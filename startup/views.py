from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import *
from .serializers import *
from django.db.models import Max
import boto3
from fundii_backend.settings import AWS_STORAGE_BUCKET_NAME
from rest_framework.permissions import IsAuthenticated
from botocore.exceptions import ClientError

class ImportantListsAPIView(APIView):
    
    def get(self, request):

        industries = Industry.objects.all()
        industry_serializer = IndustrySerializer(industries, many=True)
        
        data = {
            "industry": industry_serializer.data,
        }
        
        return Response(data=data)  # Replace `data` with the response data you want to send back

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def perform_create(self, serializer):
        serializer.save(founder=self.request.user)

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyByFounderView(APIView):
    serializer_class = CompanySerializer

    def get(self, request):
        current_user = request.user
        latest_company_id = Company.objects.filter(founder=current_user).aggregate(latest_id=Max('id'))['latest_id']
        print(latest_company_id)
        company = Company.objects.get(id=latest_company_id)
        serializer = self.serializer_class(company)
        return Response(serializer.data)