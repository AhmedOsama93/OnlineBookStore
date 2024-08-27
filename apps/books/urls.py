from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.books.views.books_views import BookListView, BookDetailView
from apps.books.views.reviews_views import ReviewCreateView, ReviewListView

urlpatterns = [ 
    path('', BookListView.as_view(), name='book-list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:book_id>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('<int:book_id>/reviews/create/', ReviewCreateView.as_view(), name='review-create'),

]
