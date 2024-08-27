from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.books.views.books_views import BookListView, BookDetailView
from apps.books.views.reviews_views import ReviewCreateView, ReviewListView

schema_view = get_schema_view(
    openapi.Info(
        title="Online Book Store API",
        default_version='v1',
        description="API documentation for the Online Book Store",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@bookstore.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [ 
    path('', BookListView.as_view(), name='book-list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:book_id>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('<int:book_id>/reviews/create/', ReviewCreateView.as_view(), name='review-create'),

]
