from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.books.models import Review


@receiver(pre_save, sender=Review)
def update_book_avg_rate(sender, instance, create=True, *args, **kwargs):
    book = instance.book
    book.sum_rate += instance.rate
    if create:
        book.count_reviews += 1
    else:
        old_rate = Review.objects.get(pk=instance.pk).rate
        book.sum_rate -= old_rate
    book.save()
