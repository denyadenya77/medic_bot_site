from django.urls import reverse
from django.views.generic import CreateView, ListView
from .models import Route


class OneTimeRouteCreateView(CreateView):
    model = Route
    template_name = 'one_time_route_creation.html'
    fields = ['user', 'date_and_time', 'start_point', 'finish_point']

    def get_success_url(self):
        return reverse('one-time-route-creation')


class RegularRouteCreateView(CreateView):
    model = Route
    template_name = 'regular_route_creation.html'
    fields = ['user', 'start_point', 'finish_point']

    def get_success_url(self):
        return reverse('regular-route-creation')


class GetRoutesListView(ListView):
    model = Route
    context_object_name = 'routes'
    template_name = 'filtered_routes.html'

