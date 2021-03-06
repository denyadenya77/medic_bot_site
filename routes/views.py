from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RouteSerializer, GetSimilarRoutesSerializer
from .models import Route
from users.models import ServiceUser
import datetime
from django.db.models import Q

from medic_bot_site.settings import VARS


class RouteViewSet(viewsets.ModelViewSet):
    """Endpoint for viewing and creating user routes"""

    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def perform_create(self, serializer):
        """Method for creating routes. Takes a user's telegram-id
         to create a one-to-many relationship"""
        telegram_id = serializer.validated_data['user']
        user = ServiceUser.objects.get(telegram_id=telegram_id)
        serializer.save(user=user)


class GetRoutes(APIView):
    """Endpoint to get similar routes"""

    def get_time(self, date_and_time):
        """method to create datetime objects to use in filtering"""
        arrival_time = datetime.datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')
        min_time = arrival_time - datetime.timedelta(minutes=VARS.get('timedelta_in_minutes'))
        max_time = arrival_time + datetime.timedelta(minutes=VARS.get('timedelta_in_minutes'))
        return min_time, max_time

    def get_medic_routes(self, **kwargs):
        """method to get similar routes for driver"""

        # filter with date_and_time__range, if time is known
        if kwargs.get('min_time'):
            routes = Route.objects.filter(Q(date_and_time__range=(kwargs['min_time'], kwargs['max_time'])) |
                                          Q(date_and_time=None),
                                          user__type='doctor',
                                          start_point__distance_lt=(kwargs['start_point'],
                                                                    Distance(km=VARS.get('points_distance'))))
        else:
            routes = Route.objects.filter(user__type='doctor',
                                          start_point__distance_lt=(kwargs['start_point'],
                                                                    Distance(km=VARS.get('points_distance'))))
        return routes

    def get_driver_routes(self, **kwargs):
        """method to get similar routes for doctor"""

        # filter with date_and_time__range, if time is known
        if kwargs.get('min_time'):
            routes = Route.objects.filter(Q(date_and_time__range=(kwargs['min_time'], kwargs['max_time'])) |
                                          Q(date_and_time=None),
                                          user__type='driver',
                                          start_point__distance_lt=(kwargs['start_point'],
                                                                    Distance(km=VARS.get('points_distance'))))
        else:
            routes = Route.objects.filter(user__type='driver',
                                          start_point__distance_lt=(kwargs['start_point'],
                                                                    Distance(km=VARS.get('points_distance'))))
        return routes

    def get(self, request):
        """Method for getting a list of routes that match at the start point"""

        # getting sequence of request user
        request_user = ServiceUser.objects.get(telegram_id=request.data['telegram_id'])
        # creating a Point object to filter
        start_point = Point(request.data['start_point']['longitude'], request.data['start_point']['latitude'])

        # creating a timedelta
        if request.data.get('date_and_time'):
            min_time, max_time = self.get_time(request.data['date_and_time'])
        else:
            min_time, max_time = None, None

        # filtering the table with a specific user type
        if request_user.type == 'driver':
            routes = self.get_medic_routes(start_point=start_point,
                                           min_time=min_time,
                                           max_time=max_time)
        else:
            routes = self.get_driver_routes(start_point=start_point,
                                            min_time=min_time,
                                            max_time=max_time)

        serializer = GetSimilarRoutesSerializer(routes, many=True)
        return Response(serializer.data)
