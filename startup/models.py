from django.db import models
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from user.models import User
from utils.utils import generate_unique_filename

# Create your models here.

def generate_cover_photo_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'cover_photo')

def generate_pitch_video_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'pitch_video')

def generate_unsigned_nda_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'unsigned_nda')

def generate_pitch_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'pitch')

def generate_signed_nda_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'signed_nda')


FUNDING_ROUNDS = (
        ('seed', 'Seed Round'),
        ('series_a', 'Series A'),
        ('series_b', 'Series B'),
        ('series_c', 'Series C'),
        ('pre_ipo', 'Pre-IPO'),
    )

class Team(models.Model):

    name = models.CharField(max_length=255,null=True, blank=True)
    role = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField()
    accomplishment = models.CharField(max_length=255,null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    history = HistoricalRecords()
    founder = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Industry(models.Model):
    name= models.CharField(max_length=30)

class Company(models.Model):

    upload_directory = 'startup/company/'

    history = HistoricalRecords()
    founder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    industry = models.ManyToManyField(to=Industry)
    stage = models.CharField(max_length=10, choices=FUNDING_ROUNDS, null=True, blank=True)
    audience = models.BigIntegerField(default=0,null=True, blank=True)
    raised_amount = models.BigIntegerField(null=True, blank=True)
    pitch_title = models.CharField(max_length=5000,null=True, blank=True)
    business_description = models.CharField(max_length=10000,null=True, blank=True)
    company_highlights = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    story_description = models.CharField(max_length=1000,null=True, blank=True)
    minimum_amount = models.IntegerField(null=True, blank=True)
    maximum_amount = models.IntegerField(null=True, blank=True)
    valuation = models.IntegerField(null=True, blank=True)
    percentage = models.IntegerField(null=True, blank=True)
    unsigned_nda = models.FileField(upload_to=generate_unsigned_nda_filename, null=True, blank=True)
    signed_nda = models.FileField(upload_to=generate_signed_nda_filename,null=True, blank=True)
    step_one = models.BooleanField(default=False)
    step_two = models.BooleanField(default=False)
    step_three = models.BooleanField(default=False)
    cover_photo = models.FileField(upload_to=generate_cover_photo_filename, null=True, blank=True)
    pitch_video = models.FileField(upload_to=generate_pitch_video_filename, null=True, blank=True)
    pitch = models.FileField(upload_to=generate_pitch_filename, null=True, blank=True)