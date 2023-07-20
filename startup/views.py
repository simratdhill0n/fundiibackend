from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.db.models import Max
from rest_framework.permissions import IsAuthenticated
from utils.amazon_utils import generate_presigned_url  # Replace `data` with the response data you want to send back

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def perform_create(self, serializer):
        serializer.save(founder=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompanyGetSerializer
        elif self.request.method == 'POST':
            return CompanyCreateSerializer
        return CompanySerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Include the details of the founder and teammates for each company
        for data in serializer.data:
            company = Company.objects.get(id=data['id'])
            founder_data = {
                'first_name': company.founder.first_name,
                'family_name': company.founder.last_name,
                'email': company.founder.email,
                'username': company.founder.username,
                'date_joined': company.founder.date_joined,
                'last_login': company.founder.last_login
            }
            teammates_queryset = Teammate.objects.filter(user=company.founder)
            teammates_serializer = TeammateSerializer(teammates_queryset, many=True)
            teammates_data = teammates_serializer.data

            data['founder'] = founder_data
            data['teammates'] = teammates_data

        return Response(serializer.data)

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompanyRetrieveSerializer
        return super().get_serializer_class()

class CompanyByFounderView(APIView):
    serializer_class = CompanyGetSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user
        latest_company_id = Company.objects.filter(founder=current_user).aggregate(latest_id=Max('id'))['latest_id']
        company = Company.objects.get(id=latest_company_id)

        # Get the data of the founder
        founder_data = {
            'first_name': company.founder.first_name,
            'family_name': company.founder.last_name,
            'email': company.founder.email,
            'username': company.founder.username,
            'date_joined':company.founder.date_joined,
            'last_login':company.founder.last_login
        }

        # Get the data of all teammates where user == founder
        teammates_queryset = Teammate.objects.filter(user=company.founder)
        teammates_data = [
            {
                'first_name': teammate.first_name,
                'family_name': teammate.family_name,
                'age':teammate.age,
                'country_of_residence':teammate.country_of_residence,
                'education_level':teammate.education_level,
                'email':teammate.email,
                'nationality':teammate.nationality,
                'phone_number':teammate.phone_number,
                'linkedin_page':teammate.linkedin_page,
                'position_at_company':teammate.position_at_company,
                'id':teammate.pk
            }
            for teammate in teammates_queryset
        ]

        # Serialize the company data
        serializer = self.serializer_class(company)
        data = serializer.data

        # Include the founder and teammates data in the response
        data['founder'] = founder_data
        data['teammates'] = teammates_data

        return Response(data)


class TeammateListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TeammateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Teammate.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TeammateGetSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.request.method == 'GET':
            # Filter the queryset by the current user for GET requests
            current_user = self.request.user
            queryset = Teammate.objects.filter(user=current_user)
            return queryset
        return self.queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class TeammateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeammateSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Teammate.objects.all()

    def get_queryset(self):
        return super().get_queryset()

class TeammateBulkUpdateAPIView(APIView):
    def patch(self, request):
        teammates_data = request.data

        for data in teammates_data:
            teammate_id = data.get('id')
            if teammate_id is not None:
                try:
                    teammate = Teammate.objects.get(id=teammate_id)
                    serializer = TeammateSerializer(teammate, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=400)
                except Teammate.DoesNotExist:
                    return Response({"error": f"Teammate with ID {teammate_id} does not exist"}, status=404)

        return Response({"message": "Bulk update successful"}, status=200)
