from apps.books.models import Book, Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'book', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'book', 'created_at']

    def validate_rating(self, value):
        """Ensure the rating is between 1 and 5."""
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        validated_data['book_id'] = self.context['book_id']
        return super().create(validated_data)


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'content']
