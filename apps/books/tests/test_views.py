from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from apps.books.models import Book
from apps.books.serializers import BookSerializer, BookListSerializer


class BookViewsTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        self.book1 = Book.objects.create(
            title='Book 1',
            author='Author 1',
            description='Description 1',
            content='Content 1'
        )
        self.book2 = Book.objects.create(
            title='Book 2',
            author='Author 2',
            description='Description 2',
            content='Content 2'
        )

    def test_book_list_view(self):
        url = reverse('book-list')
        response = self.client.get(url)

        serializer = BookListSerializer([self.book1, self.book2], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_book_detail_view(self):
        url = reverse('book-detail', kwargs={'book_id': self.book1.id})  # Adjust the name if necessary
        response = self.client.get(url)

        serializer = BookSerializer(self.book1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_book_detail_view_not_found(self):
        url = reverse('book-detail', kwargs={'book_id': 999})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
