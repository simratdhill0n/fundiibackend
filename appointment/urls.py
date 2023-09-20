from django.urls import path
from . import views

urlpatterns = [
    path('staff-availability', views.StaffAvailabilityViewSet.as_view(), name='staff-availability'),
    path('appointments', views.AppointmentViewSet.as_view(), name='staff-availability'),
]
