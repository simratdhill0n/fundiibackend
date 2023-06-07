from django.urls import path
from . import views

urlpatterns = [
    path('important_lists/', views.ImportantListsAPIView.as_view() , name="important_lists"),
]