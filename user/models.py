from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models, migrations
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from datetime import timedelta
from django.utils.timezone import utc

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    history = HistoricalRecords()

    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)

class Appointment(models.Model):

    staff = models.ManyToManyField(to='user.User', limit_choices_to={'is_staff':True})
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_startups = models.ManyToManyField(to="startup.Company", related_name="available_startups")
    investor = models.ForeignKey(to="investor.Investor", on_delete=models.SET_NULL, null=True)
    selected_startup = models.ForeignKey(to="startup.Company", on_delete=models.SET_NULL, null= True, related_name="selected_startup")
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        
        self.end_time = self.start_time + timedelta(minutes=30)

        if not self.staff.exists():

            self.staff.add(User.objects.filter(is_superuser=True).first())

        if not self.start_time.tzinfo:
            self.start_time = self.start_time.replace(tzinfo=utc)
        if not self.end_time.tzinfo:
            self.end_time = self.end_time.replace(tzinfo=utc)

        super().save(*args, **kwargs)