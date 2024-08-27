from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from apps.books.models import Book
from apps.books.serializers import BookSerializer


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
        book = get_object_or_404(Book, pk=kwargs.get('book_id'))
        serializer = self.serializer_class(book)
        return Response(serializer.data)
