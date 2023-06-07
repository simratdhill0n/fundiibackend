from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users'),
    path('current/', views.CurrentUserDetailAPIView.as_view(), name='current_user'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('api/groups/', views.GroupList.as_view(), name= 'groups'),
    path('api/groups/<int:pk>/', views.GroupDetail.as_view(), name='group_detail'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('check-unique/', views.CheckUniqueAPI.as_view(), name='check_unique'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]