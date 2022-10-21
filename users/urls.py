from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListView, UserUpdateView, UserCreateView, UserRetrieveView, \
    UserDestroyView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserRetrieveView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDestroyView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
