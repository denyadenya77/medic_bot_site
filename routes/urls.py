from django.urls import path
from .views import OneTimeRouteCreateView, RegularRouteCreateView, GetRoutesListView


urlpatterns = [
    path('create_one/', OneTimeRouteCreateView.as_view(), name='one-time-route-creation'),
    path('create_regular/', RegularRouteCreateView.as_view(), name='regular-route-creation'),
    path('filtered_list/', GetRoutesListView.as_view(), name='filtered-routes'),
]
