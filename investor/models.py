from django.db import models
from user.models import User
from utils.choicefields import FUNDING_ROUNDS, INVESTOR_TYPES, REGION_CHOICES, INDUSTRY_CHOICES, VERTICAL_CHOICES
from utils.utils import generate_identity_proof_filename, generate_organisation_document_filename, generate_profile_picture_filename
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.

class Investor(models.Model):

    upload_directory = 'investor/'

    owner = models.ForeignKey(to= User, on_delete=models.CASCADE, null=True, blank= True)
    organisation_document  = models.FileField(upload_to=generate_organisation_document_filename,null=True, blank=True)
    birthdate = models.DateField(default=timezone.now)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    identity_proof = models.FileField(upload_to=generate_identity_proof_filename,null=True, blank=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    address_unit = models.CharField(max_length=100, null=True)
    address_street = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=10)
    annual_income_min = models.IntegerField(default=0)
    annual_income_max = models.IntegerField(default=0)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_address = models.CharField(max_length= 255, null=True, blank= True)
    website = models.URLField(null=True, blank= True)
    investor_type = models.CharField(max_length=100, choices=INVESTOR_TYPES)
    stage_of_investment = ArrayField(
        models.CharField(choices=FUNDING_ROUNDS, max_length=100, blank=True),
        null=True,
        blank=True
    )
    industry = ArrayField(
        models.CharField(choices=INDUSTRY_CHOICES, max_length=100, blank=True), 
        blank=True,
        null=True
    )
    vertical = ArrayField(models.CharField(max_length=64, choices=VERTICAL_CHOICES), blank= True, null=True)
    interested_region = ArrayField(
        models.CharField(choices=REGION_CHOICES, max_length=100, blank=True),
        null=True,
        blank=True
    )
    minimum_investment = models.IntegerField()
    maximum_investment = models.IntegerField()

    # Risk analysis

    persona = models.BooleanField(default=False)
    aws_identity_verification = models.BooleanField(default=False)

    profile_picture = models.FileField(upload_to=generate_profile_picture_filename, null=True, blank=True)

    class Meta:
        unique_together = ('owner',)