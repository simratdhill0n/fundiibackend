from rest_framework import generics
from .models import Investor
from .serializers import InvestorSerializer
from rest_framework.permissions import IsAuthenticated

class InvestorListCreateView(generics.ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InvestorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer