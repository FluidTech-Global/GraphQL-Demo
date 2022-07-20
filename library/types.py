from dataclasses import fields
import graphene

from graphene_django import DjangoObjectType

from library.models import Author, Book
from graphqldemo.utils import PaginatedObjectType


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"


class PaginatedAuthorType(PaginatedObjectType):
    objects = graphene.List(
        AuthorType,
        description="List of authors (AuthorType)."
    )


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"
