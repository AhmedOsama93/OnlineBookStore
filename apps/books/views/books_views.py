from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from apps.books.models import Book
from apps.books.serializers import BookSerializer, BookListSerializer

from rest_framework.permissions import IsAuthenticated


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: BookListSerializer(many=True),
            400: 'Bad Request',
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.prefetch_related('reviews')

    @swagger_auto_schema(
        responses={
            200: BookSerializer,
            403: 'Not authorized',
            404: 'Book not found',
        },
    )
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(
            self.get_queryset(),
            pk=kwargs.get('book_id')
        )
        serializer = self.serializer_class(book)
        return Response(serializer.data)
