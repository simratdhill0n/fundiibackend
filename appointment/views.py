from rest_framework import viewsets
from .models import StaffAvailability, Appointment
from .serializers import StaffAvailabilitySerializer, AppointmentSerializer

class StaffAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = StaffAvailability.objects.all()
    serializer_class = StaffAvailabilitySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer