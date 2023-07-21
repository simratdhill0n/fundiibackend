from django.db import models
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from utils.utils import (generate_avtar_filename, generate_pitch_filename, generate_pitch_video_filename, generate_signed_ncnd_filename, validate_1000_word_limit, validate_100_word_limit, 
                         validate_200_word_limit, validate_150_word_limit, generate_company_proof_filename, generate_identity_proof_filename,
                         generate_cover_photo_filename, generate_signed_nda_filename, generate_unsigned_nda_filename, generate_unique_filename)
import datetime

from utils.choicefields import (FUNDING_ROUNDS, LAUNCH_STATUS_CHOICES, INDUSTRY_CHOICES, VERTICAL_CHOICES, SALES_TYPE_CHOICES, TARGET_CUSTOMER_LOCATIONS,
                                AGE_CHOICES, EDUCATION_CHOICES)

# Create your models here.

class Company(models.Model):
    
    upload_directory = 'startup/company/'
    history = HistoricalRecords()
    step_one = models.BooleanField(default=False)
    step_two = models.BooleanField(default=False)
    step_three = models.BooleanField(default=False)
    founder = models.ForeignKey(to='user.User', on_delete=models.CASCADE, null=True)

    # step 1 fields

    project_title = models.CharField(max_length=64, blank=True)
    business_description = models.CharField(validators=(validate_100_word_limit,), blank=True)
    launch_status = models.CharField(max_length=20, choices=LAUNCH_STATUS_CHOICES, default='no')
    industry = ArrayField(
        models.CharField(choices=INDUSTRY_CHOICES, max_length=100, blank=True), 
        blank=True,
        null=True
    )
    vertical = ArrayField(models.CharField(max_length=64, choices=VERTICAL_CHOICES), blank= True, null=True)
    incorporation_location = models.CharField(max_length= 100, blank=True)
    headquarters_location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True, null=True)

    # step 2 fields

    overview = models.CharField(validators=(validate_1000_word_limit,), blank=True)
    pitch = models.FileField(upload_to=generate_pitch_filename, blank=True)
    stage = models.CharField(max_length=100, choices=FUNDING_ROUNDS, blank=True)
    sales_type = models.CharField(max_length=10, choices=SALES_TYPE_CHOICES, default='other')
    business_model = models.CharField(validators=( validate_200_word_limit,), blank=True)
    revenue_record_six_month = models.IntegerField(default=0)
    target_customers_location = models.CharField(max_length=30, choices=TARGET_CUSTOMER_LOCATIONS, blank=True)
    problem_solution = models.CharField(validators=(validate_200_word_limit,), blank=True)
    regional_competitors = models.CharField(validators=(validate_100_word_limit,), blank=True)
    international_competitors = models.CharField(validators=(validate_100_word_limit,), blank=True)
    competitive_advantage = models.CharField(validators=(validate_150_word_limit,), blank=True)
    monthly_burn_rate = models.IntegerField(default=0)
    current_cash_balance = models.IntegerField(default=0)
    already_raised_money = models.BooleanField(default=False)
    number_of_full_time_employees = models.PositiveIntegerField(default=0)
    number_of_part_time_employees = models.PositiveIntegerField(default=0)
    past_companies_bool = models.BooleanField(default=False)
    past_companies = ArrayField(models.CharField(max_length=64), blank=True, null=True)
    pitch_deck = models.FileField(upload_to=generate_pitch_video_filename, null=True)

    # verfification fields

    risk_analysis = models.BooleanField(default=False)
    persona = models.BooleanField(default=False)
    aws_identity_verification = models.BooleanField(default=False)

    # step 3 fields

    signed_ncnd = models.FileField(upload_to=generate_signed_ncnd_filename,null=True, blank=True)

    #interested investors

    interested_investors = models.ManyToManyField(to= 'investor.Investor')

    avtar = models.FileField(upload_to= generate_avtar_filename , null=True, blank=True)

    class Meta:
        unique_together = ('founder',)

class Teammate(models.Model):

    first_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    age = models.IntegerField(choices=AGE_CHOICES)
    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    country_of_residence = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    linkedin_page = models.URLField(blank=True, null=True)
    position_at_company = models.CharField(max_length=50)
    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.first_name} {self.family_name}"

class Deal(models.Model):

    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    investors = models.ManyToManyField(to='investor.Investor')
    amount = models.PositiveIntegerField()
    date = models.DateTimeField()