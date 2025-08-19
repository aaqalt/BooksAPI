from rest_framework import serializers

from books.models import Category, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category",write_only=True
    )
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "published_date",
            "category",
            "category_id",
            "available_copies",
            "total_copies",
            "created_at",
        ]