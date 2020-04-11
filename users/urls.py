from django.urls import path
from .views import ServiceUserCreationView, ServiceUserDeleteView


urlpatterns = [
    path('create/', ServiceUserCreationView.as_view(), name='service-user-creation'),
    path('delete/<int:pk>', ServiceUserDeleteView.as_view(), name='service-user-deletion'),
]
