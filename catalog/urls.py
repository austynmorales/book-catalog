from django.urls import path
from .views import BookListView, PublisherListView, ReviewListView

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("publishers/", PublisherListView.as_view(), name="publisher-list"),
    path("reviews/", ReviewListView.as_view(), name="review-list"),
]