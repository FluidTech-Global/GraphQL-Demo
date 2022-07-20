from django.http import JsonResponse
from django.shortcuts import render

from library.models import Author, Book


def fetch_all_authors(request):
    """
    REST ednpoint to fetch all authors.
    """

    authors = Author.objects.all()

    return_data = [
        {"public_id": author.public_id, "first_name": author.first_name, "last_name": author.last_name, "date_of_birth": author.date_of_birth} for author in authors
    ]

    return JsonResponse({
        "data": return_data
    })


def fetch_single_author(request, author_id):
    """
    REST ednpoint to fetch single author details.
    """

    author = Author.objects.filter(
        public_id=author_id
    ).first()

    return_data = [
        {
            "public_id": author.public_id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "date_of_birth": author.date_of_birth
        }
    ]

    return JsonResponse({
        "data": return_data
    })


def fetch_single_author(request, author_id):
    """
    REST ednpoint to fetch single author details.
    """

    author = Author.objects.filter(
        public_id=author_id
    ).first()

    if not author:
        return JsonResponse({
            "message": "Requested author does not exist."
        }, status=404)

    return_data = [
        {
            "public_id": author.public_id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "date_of_birth": author.date_of_birth
        }
    ]

    return JsonResponse({
        "data": return_data
    })


def fetch_single_author_with_books(request, author_id):
    """
    REST ednpoint to fetch single author details with books.
    """

    author = Author.objects.filter(
        public_id=author_id
    ).prefetch_related(
        "book_set"
    ).first()

    if not author:
        return JsonResponse({
            "message": "Requested author does not exist."
        }, status=404)

    books = [{"public_id": book.public_id, "title": book.title, "isbn": book.isbn} for book in author.book_set.all()]

    return_data = [
        {
            "public_id": author.public_id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "date_of_birth": author.date_of_birth,
            "books": books
        }
    ]

    return JsonResponse({
        "data": return_data
    })
