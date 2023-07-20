from rest_framework import serializers
from .models import Investor
from utils.amazon_utils import generate_presigned_url
from user.serializers import UserGetSerializer

class InvestorSerializer(serializers.ModelSerializer):

    organisation_document_presigned_url = serializers.SerializerMethodField()
    identity_proof_presigned_url = serializers.SerializerMethodField()
    profile_picture_presigned_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Investor
        fields = "__all__"
        read_only_fields = ['owner']  # Marking owner field as read-only

    def get_organisation_document_presigned_url(self, obj):
        return generate_presigned_url(obj.organisation_document.name) if obj.organisation_document else None
    
    def get_identity_proof_presigned_url(self, obj):
        return generate_presigned_url(obj.identity_proof.name) if obj.identity_proof else None
    
    def get_profile_picture_presigned_url(self, obj):
        return generate_presigned_url(obj.profile_picture.name) if obj.profile_picture else None
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Populate owner field with current user if it's a GET request
        representation['owner'] = UserGetSerializer(instance.owner).data
        
        return representation
