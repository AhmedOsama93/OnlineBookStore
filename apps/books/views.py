from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.books.models import Book, Review
from apps.books.serializers import BookSerializer, ReviewSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(
        responses={
            200: BookSerializer(many=True),
            400: 'Bad Request',
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer

    @swagger_auto_schema(
        responses={
            200: BookSerializer,
            403: 'Not authorized',
            404: 'Book not found',
        },
    )
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs.get('book_id'))
        serializer = self.serializer_class(book)
        return Response(serializer.data)


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ReviewSerializer,
        responses={
            201: ReviewSerializer,
            400: 'Bad Request',
            401: 'Unauthorized',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(context={'request': request, 'book_id': kwargs.get('book_id')}, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
