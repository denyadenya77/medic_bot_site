from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import ServiceUser


class ServiceUserCreationView(CreateView):
    model = ServiceUser
    template_name = 'service_user_creation.html'
    fields = ['telegram_id', 'type', 'first_name', 'last_name', 'phone_number']

    def get_success_url(self):
        return reverse('service-user-creation')


class ServiceUserDeleteView(DeleteView):
    model = ServiceUser
    template_name = 'service_user_deletion.html'
    success_url = reverse_lazy('service-user-creation')

