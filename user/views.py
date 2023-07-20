from rest_framework import generics
from .models import User, Group
from .serializers import UserSerializer, TokenBlacklistSerializer, GroupSerializer, CurrentUserSerializer, CustomTokenObtainPairSerializer
from .permissions import CreateUserPermission
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import datetime
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  
        
def send_verfication_email(request, user):
    to_email = request.data.get('email')
    current_site = get_current_site(request)  
    mail_subject = 'Activation link has been sent to your email id'  
    message = render_to_string('acc_active_email.html', {  
        'user': user,  
        'domain': current_site.domain,  
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
        'token':account_activation_token.make_token(user),  
    })
    email = EmailMessage(  
                mail_subject, message, to=[to_email]
    )  
    email.send()  

class LogoutAPIView(APIView):
    serializer_class = TokenBlacklistSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        
        user = User.objects.get(username=username)

        group_id = request.data.get('group')
        
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({'detail': 'Invalid group'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.groups.filter(id=group_id).exists() and not user.is_superuser:
            return Response({'detail': f'User does not belong to {group.name} group'}, status=status.HTTP_403_FORBIDDEN)

        user.last_login = datetime.datetime.now()

        user.save()

        return super().post(request, *args, **kwargs)

class CustomTokenRefreshView(TokenRefreshView):
    pass

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CreateUserPermission | IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract group ID from request data
        group_id = request.data.get('group')

        # Check if the group ID exists
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({'detail': 'Invalid group ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the user instance
        user = serializer.save()

        # Assign the group to the user
        user.groups.add(group)

        headers = self.get_success_headers(serializer.data)

        send_verfication_email(request=request, user=user)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CheckUniqueAPI(APIView):

    def get(self, request):
        
        field_name = request.GET.get('field_name')
        field_value = request.GET.get('field_value')

        # Check if the field value is unique for the given field name
        duplicate = User.objects.filter(**{field_name: field_value}).exists()

        return Response(duplicate)
    
class CurrentUserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user