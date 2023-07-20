from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Investor
from .serializers import InvestorSerializer
from rest_framework.permissions import IsAuthenticated
from utils.amazon_utils import generate_presigned_url
from django.db.models import Max

class InvestorListCreateView(generics.ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self):
        obj = super().get_object()
        obj.organisation_document_presigned_url = generate_presigned_url(obj.organisation_document.name) if obj.organisation_document else None
        obj.identity_proof_presigned_url = generate_presigned_url(obj.identity_proof.name) if obj.identity_proof else None
        return obj

class InvestorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

    def get_object(self):
        obj = super().get_object()
        obj.organisation_document_presigned_url = generate_presigned_url(obj.organisation_document.name) if obj.organisation_document else None
        obj.identity_proof_presigned_url = generate_presigned_url(obj.identity_proof.name) if obj.identity_proof else None
        return obj

class InvestorByOwnerView(APIView):
    serializer_class = InvestorSerializer

    def get(self, request):
        current_user = request.user
        latest_investor_id = Investor.objects.filter(owner=current_user).aggregate(latest_id=Max('id'))['latest_id']
        investor = Investor.objects.get(id=latest_investor_id)
        serializer = self.serializer_class(investor)
        return Response(serializer.data)