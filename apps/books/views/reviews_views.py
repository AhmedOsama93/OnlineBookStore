from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from apps.books.models import Review, Book
from apps.books.serializers import ReviewSerializer


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


class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: ReviewSerializer(many=True),
            404: 'Book not found',
        },
        response_body=ReviewSerializer
    )
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs.get('book_id'))
        reviews = Review.objects.filter(book=book)
        serializer = self.serializer_class(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
