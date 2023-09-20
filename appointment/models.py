from django.db import models
from datetime import timedelta
from django.utils.timezone import utc
from django.apps import apps

from user.models import User
from startup.models import Company
from investor.models import Investor

user_model = User
startup_model = Company
investor_model = Investor

# Create your models here.
class StaffAvailability(models.Model):

    staff = models.ForeignKey(to=user_model, limit_choices_to={'is_staff':True}, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    availabity = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        
        self.end_time = self.start_time + timedelta(minutes=30)

        if not self.staff:
            self.staff = user_model.objects.filter(is_superuser=True).first()
        if not self.start_time.tzinfo:
            self.start_time = self.start_time.replace(tzinfo=utc)
        if not self.end_time.tzinfo:
            self.end_time = self.end_time.replace(tzinfo=utc)

        super().save(*args, **kwargs)

class Appointment(models.Model):

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    startup = models.ForeignKey(to=startup_model, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    staff = models.ManyToManyField(to=user_model, limit_choices_to={'is_staff':True})
    investor = models.ManyToManyField(to=investor_model)

    def save(self, *args, **kwargs):
        
        self.end_time = self.start_time + timedelta(minutes=30)
        if not self.start_time.tzinfo:
            self.start_time = self.start_time.replace(tzinfo=utc)
        if not self.end_time.tzinfo:
            self.end_time = self.end_time.replace(tzinfo=utc)

        super().save(*args, **kwargs)