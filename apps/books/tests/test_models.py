from django.test import TestCase
from django.contrib.auth.models import User
from apps.books.models import Book, Review


class BookModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(
            title='Test Book',
            author='Author Name',
            description='This is a test book description.',
            content='This is test book content.',
            sum_rate=10,
            count_reviews=2
        )

    def test_avg_rate(self):
        self.assertEqual(self.book.avg_rate, 5)

    def test_avg_rate_no_reviews(self):
        book_no_reviews = Book.objects.create(
            title='Another Test Book',
            author='Author Name',
            description='This is another test book description.',
            content='This is another test book content.'
        )
        self.assertEqual(book_no_reviews.avg_rate, 0)

    def test_str_method(self):
        self.assertEqual(str(self.book), 'Test Book')


class ReviewModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(
            title='Test Book',
            author='Author Name',
            description='This is a test book description.',
            content='This is test book content.'
        )
        self.review = Review.objects.create(
            user=self.user,
            book=self.book,
            rate=5,
            comment='Great book!'
        )

    def test_review_creation(self):
        self.assertEqual(self.review.book, self.book)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.rate, 5)
        self.assertEqual(self.review.comment, 'Great book!')

    def test_str_method(self):
        # Test the __str__ method of Review
        self.assertEqual(str(self.review), 'testuser - Test Book')
