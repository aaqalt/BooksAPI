from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    BookListCreateView, BookDetailView
)

urlpatterns = [
    # Category URLs
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    # Book URLs
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
