from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "user", "book", "rating", "comment", "created_at"]
