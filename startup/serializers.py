from rest_framework import serializers
from .models import *
from utils.amazon_utils import generate_presigned_url

class TeammateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        exclude = ('user',)

class TeammateGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['founder', 'interested_investors']


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    founder = serializers.SerializerMethodField()
    teammates = serializers.SerializerMethodField()
    pitch_presigned_url = serializers.SerializerMethodField()
    pitch_deck_presigned_url = serializers.SerializerMethodField()
    signed_ncnd_presigned_url = serializers.SerializerMethodField()
    avtar_presigned_url = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'step_one', 'step_two', 'step_three', 'project_title', 'business_description', 'launch_status', 'industry', 'vertical', 'incorporation_location', 'headquarters_location', 'website', 'overview', 'pitch', 'stage', 'sales_type', 'business_model', 'revenue_record_six_month', 'target_customers_location', 'problem_solution', 'regional_competitors', 'international_competitors', 'competitive_advantage', 'monthly_burn_rate', 'current_cash_balance', 'already_raised_money', 'number_of_full_time_employees', 'number_of_part_time_employees', 'past_companies_bool', 'past_companies', 'pitch_deck', 'risk_analysis', 'persona', 'aws_identity_verification', 'signed_ncnd', 'founder', 'teammates', 'pitch_presigned_url', 'pitch_deck_presigned_url', 'signed_ncnd_presigned_url']

    def get_founder(self, instance):
        founder = instance.founder
        return {
            'first_name': founder.first_name,
            'family_name': founder.last_name,
            'email': founder.email,
            'username': founder.username,
            'date_joined': founder.date_joined,
            'last_login': founder.last_login
        }

    def get_teammates(self, instance):
        teammates = Teammate.objects.filter(user=instance.founder)
        return TeammateSerializer(teammates, many=True).data

    def get_pitch_presigned_url(self, instance):
        return generate_presigned_url(instance.pitch.name) if instance.pitch else None

    def get_pitch_deck_presigned_url(self, instance):
        return generate_presigned_url(instance.pitch_deck.name) if instance.pitch_deck else None

    def get_signed_ncnd_presigned_url(self, instance):
        return generate_presigned_url(instance.signed_ncnd.name) if instance.signed_ncnd else None
    
    def get_avtar_presigned_url(self, obj):
        return generate_presigned_url(obj.avtar.name) if obj.avtar else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['founder'] = self.get_founder(instance)
        data['teammates'] = self.get_teammates(instance)
        data['pitch_presigned_url'] = self.get_pitch_presigned_url(instance)
        data['pitch_deck_presigned_url'] = self.get_pitch_deck_presigned_url(instance)
        data['signed_ncnd_presigned_url'] = self.get_signed_ncnd_presigned_url(instance)
        data['avtar_presigned_url'] = self.get_avtar_presigned_url(instance)
        return data

class CompanyGetSerializer(serializers.ModelSerializer):
    pitch_presigned_url = serializers.SerializerMethodField()
    pitch_deck_presigned_url = serializers.SerializerMethodField()
    signed_ncnd_presigned_url = serializers.SerializerMethodField()
    avtar_presigned_url = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_pitch_presigned_url(self, obj):
        return generate_presigned_url(obj.pitch.name) if obj.pitch else None

    def get_pitch_deck_presigned_url(self, obj):
        return generate_presigned_url(obj.pitch_deck.name) if obj.pitch_deck else None

    def get_signed_ncnd_presigned_url(self, obj):
        return generate_presigned_url(obj.signed_ncnd.name) if obj.signed_ncnd else None
    
    def get_avtar_presigned_url(self, obj):
        return generate_presigned_url(obj.avtar.name) if obj.avtar else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['pitch_presigned_url'] = self.get_pitch_presigned_url(instance)
        data['pitch_deck_presigned_url'] = self.get_pitch_deck_presigned_url(instance)
        data['signed_ncnd_presigned_url'] = self.get_signed_ncnd_presigned_url(instance)
        data['avtar_presigned_url'] = self.get_avtar_presigned_url(instance)
        return data
