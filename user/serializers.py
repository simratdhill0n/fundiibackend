from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status

class TokenBlacklistSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.get('refresh_token')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception as e:
                raise serializers.ValidationError('Token is invalid or expired')
        else:
            raise serializers.ValidationError('Refresh token is required')

        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        encrypted_password = make_password(password)
        validated_data['password'] = encrypted_password
        return super().create(validated_data)

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    group = serializers.IntegerField()