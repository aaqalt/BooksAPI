from books.views import UserListCreateAPIView, UserDetailAPIView, LoginAPIView, RegisterUserAPIView
from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    BookListCreateView, BookDetailView
)

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('register/',RegisterUserAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    # Category URLs
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    # Book URLs
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
