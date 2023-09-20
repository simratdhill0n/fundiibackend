from .models import *
from rest_framework import serializers

class StaffAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffAvailability
        exclude = ('end_time',)

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        exclude = ('end_time',)