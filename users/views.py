from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserListSerializer, UserCreateSerializer, UserRetrieveSerializer, UserUpdateSerializer, \
    UserDestroySerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
    permission_classes = [IsAuthenticated]
