
from django.contrib import admin
from django.urls import path, include

from books.views import UserListCreateAPIView, UserDetailAPIView, LoginAPIView, RegisterUserAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('register/',RegisterUserAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
