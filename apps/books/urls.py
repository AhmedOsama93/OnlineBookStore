from apps.books.views import BookListView, BookDetailView, ReviewCreateView
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:book_id>/reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
