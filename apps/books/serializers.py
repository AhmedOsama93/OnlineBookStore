from apps.books.models import Book, Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'book', 'rate', 'comment', 'created_at']
        read_only_fields = ['user', 'book', 'created_at']

    def validate_rate(self, value):
        """Ensure the rate is between 1 and 5."""
        if not 1 <= value <= 5:
            raise serializers.ValidationError("rate must be between 1 and 5.")
        return value

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        validated_data['book_id'] = self.context['book_id']
        return super().create(validated_data)


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'avg_rate']


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'content', 'avg_rate', 'reviews']
