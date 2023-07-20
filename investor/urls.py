from django.urls import path
from . import views

urlpatterns = [
    path('investors/', views.InvestorListCreateView.as_view(), name='investor-list-create'),
    path('investors/<int:pk>/', views.InvestorRetrieveUpdateDestroyView.as_view(), name='investor-retrieve-update-destroy'),
    path('current_investor/', views.InvestorByOwnerView.as_view(), name= "company_by_owner")
]
