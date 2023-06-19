from django.urls import path
from .views import *
from django.urls import path


urlpatterns = [
    path('important_lists/', ImportantListsAPIView.as_view() , name="important_lists"),
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-retrieve-update-destroy'),
    path('company/', CompanyByFounderView.as_view(), name= "company_by_founder")
]