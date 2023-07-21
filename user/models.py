from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models, migrations
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    history = HistoricalRecords()

    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)