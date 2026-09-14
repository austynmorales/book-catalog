from django.test import TestCase
from django.urls import reverse

from .models import Publisher, Book


class BookListTests(TestCase):
    def test_book_in_database_appears_on_books_page(self):
        publisher = Publisher.objects.create(name="Test Publisher")

        Book.objects.create(
            title="Unique Testing Book",
            publisher=publisher,
            publication_year=2026,
        )

        response = self.client.get(reverse("book-list"))

        self.assertContains(response, "Unique Testing Book")

# Create your tests here.
