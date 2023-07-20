from django.urls import path
from .views import *
from django.urls import path


urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-retrieve-update-destroy'),
    path('company/', CompanyByFounderView.as_view(), name= "company_by_founder"),
    path('teammate/', TeammateListCreateAPIView.as_view(), name='teammate-list-create'),
    path('teammate/<int:pk>/', TeammateRetrieveUpdateDestroyAPIView.as_view(), name='teammate-retrieve-update-destroy'),
    path('bulk-update-teammate/', TeammateBulkUpdateAPIView.as_view(), name='bulk--update-teammate'),
]