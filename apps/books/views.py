from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import status

from apps.books.models import Book, Review
from apps.books.serializers import BookSerializer, ReviewSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=ReviewSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(context={'request': request, 'book_id': kwargs.get('book_id')}, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
