from django.db import models
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Industry(models.Model):
    name= models.CharField(max_length=30)



class Company(models.Model):

    FUNDING_ROUNDS = (
        ('seed', 'Seed Round'),
        ('series_a', 'Series A'),
        ('series_b', 'Series B'),
        ('series_c', 'Series C'),
        ('pre_ipo', 'Pre-IPO'),
    )

    history = HistoricalRecords()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    industry = models.ManyToManyField(to=Industry)
    stage = models.CharField(max_length=10, choices=FUNDING_ROUNDS)
    audience = models.BigIntegerField()
    raised_amount = models.BigIntegerField()
    pitch_title = models.CharField(max_length=5000)
    business_description = models.CharField(max_length=10000)
    company_highlights = ArrayField(models.CharField(max_length=255))
    team = ArrayField(models.JSONField())