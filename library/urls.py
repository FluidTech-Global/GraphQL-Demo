from django.urls import path

from library.views import fetch_all_authors, fetch_single_author, fetch_single_author_with_books


urlpatterns = [
    path("authors", fetch_all_authors, name="fetch_all_users"),
    path("authors/<author_id>", fetch_single_author, name="fetch_single_user"),
    path("authors/<author_id>/books", fetch_single_author_with_books, name="fetch_single_user_with_books"),
]
