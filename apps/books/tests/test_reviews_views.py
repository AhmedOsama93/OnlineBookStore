from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from apps.books.models import Book, Review
from apps.books.serializers import ReviewSerializer


class ReviewViewsTest(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a book instance
        self.book = Book.objects.create(
            title='Sample Book',
            author='Sample Author',
            description='Sample Description',
            content='Sample Content'
        )

        # Create review URLs
        self.review_create_url = reverse('review-create', kwargs={'book_id': self.book.id})
        self.review_list_url = reverse('review-list', kwargs={'book_id': self.book.id})

    def test_create_review(self):
        # Test creating a review
        data = {
            'rate': 5,
            'comment': 'Excellent book!'
        }
        response = self.client.post(self.review_create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.get().comment, 'Excellent book!')

    def test_create_review_unauthenticated(self):
        # Test creating a review without authentication
        self.client.logout()
        data = {
            'rate': 4,
            'comment': 'Good book.'
        }
        response = self.client.post(self.review_create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_reviews(self):
        # Create a review for testing
        Review.objects.create(
            user=self.user,
            book=self.book,
            rate=4,
            comment='Nice book.'
        )

        response = self.client.get(self.review_list_url)

        reviews = Review.objects.filter(book=self.book)
        serializer = ReviewSerializer(reviews, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_reviews_book_not_found(self):
        # Test listing reviews for a non-existing book
        invalid_url = reverse('review-list', kwargs={'book_id': 999})
        response = self.client.get(invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
