from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    author = models.CharField(max_length=100, verbose_name=_("Author"))
    description = models.TextField(max_length=400, verbose_name=_("Description"))
    content = models.TextField(max_length=400, verbose_name=_("Content"))
    sum_rate = models.PositiveIntegerField(verbose_name=_("Sum rete of reviews"), default=0)
    count_reviews = models.PositiveIntegerField(verbose_name=_("Count reviews"), default=0)

    def __str__(self):
        return self.title

    @property
    def avg_rate(self):
        return self.sum_rate / self.count_reviews if self.count_reviews else 0


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    rate = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['book']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
