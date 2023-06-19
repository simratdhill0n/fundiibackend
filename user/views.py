from rest_framework import generics
from .models import User, Group
from .serializers import UserSerializer, TokenBlacklistSerializer, GroupSerializer, CurrentUserSerializer
from .permissions import CreateUserPermission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import datetime


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
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        
        user = User.objects.get(username=username)

        group_id = request.data.get('group')  # Assuming the group name is provided in the request data
        
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({'detail': 'Invalid group'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.groups.filter(id=group_id).exists():
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