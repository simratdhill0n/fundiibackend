from django.db import models
from startup.models import User, Industry

# Create your models here.

INVESTOR_TYPES = (
    ('angel', 'Angel Investor'),
    ('vc', 'Venture Capitalist'),
    ('pe', 'Private Equity Firm'),
    ('hedge_fund', 'Hedge Fund'),
    ('mutual_fund', 'Mutual Fund'),
    ('investment_bank', 'Investment Bank'),
    ('family_office', 'Family Office'),
    ('pension_fund', 'Pension Fund'),
    ('endowment', 'Endowment'),
    ('foundation', 'Foundation'),
    ('corporate', 'Corporate Investor'),
    ('government', 'Government Investor'),
    ('sovereign_wealth_fund', 'Sovereign Wealth Fund'),
    ('accelerator', 'Accelerator'),
    ('incubator', 'Incubator'),
    ('crowdfunding', 'Crowdfunding Platform'),
    ('retail', 'Retail Investor'),
    ('other', 'Other'),
)

class Investor(models.Model):

    owner = models.ForeignKey(to= User, on_delete=models.CASCADE, null=True, blank= True)
    legal_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    net_worth = models.IntegerField()
    annual_income = models.IntegerField()
    birthdate = models.DateField()
    bio = models.CharField(max_length=100)
    website = models.URLField(null=True, blank= True)
    investor_type = models.CharField(max_length=50, choices=INVESTOR_TYPES)
    minimum_investment = models.IntegerField()
    maximum_investment = models.IntegerField()
    area_of_interest = models.ManyToManyField(to=Industry)