import graphene

from library.models import Author, Book
from library.mutations import AuthorMutation, BookMutation
from library.types import AuthorType, PaginatedAuthorType, BookType
from graphqldemo.utils import return_paginator


class AuthorQuery(graphene.ObjectType):
    """
    Defines queries based on the library.models.Author model
    """

    authors = graphene.List(
        AuthorType,
        description="Retrieve a list of all authors."
    )
    paginated_authors = graphene.Field(
        PaginatedAuthorType,
        page=graphene.Int(default_value=1),
        per_page=graphene.Int(default_value=30),
        description="Retrieve a paginated list of authors."
    )
    author = graphene.Field(
        AuthorType,
        id=graphene.ID(required=True),
        description="Retrieve a single author."
    )


    def resolve_authors(self, info):
        """
        Parameters
        ----------
        info : Any
            Contains useful information and is passed to all resolve methods

        Returns
        -------
        graphene.ObjectType
            A Graphene ObjectType made up of the requested data points.
        """

        authors = Author.objects.all()

        return authors


    def resolve_paginated_authors(self, info, page, per_page):
        """
        Parameters
        ----------
        info : Any
            Contains useful information and is passed to all resolve methods
        page : int, required
            Page number
        per_page : int, required
            Number of records per page

        Returns
        -------
        graphene.ObjectType
            A Graphene ObjectType made up of the requested data points.
        """

        authors = Author.objects.all()

        return return_paginator(authors, page, per_page, PaginatedAuthorType)


    def resolve_author(self, info, id):
        """
        Parameters
        ----------
        info : Any
            Contains useful information and is passed to all resolve methods
        id : str, required
            Author public ID

        Returns
        -------
        graphene.ObjectType
            A Graphene ObjectType made up of the requested data points.
        """

        author = Author.objects.filter(
            public_id=id
        ).first()

        return author


class BookQuery(graphene.ObjectType):
    """
    Defines queries based on the library.models.Book model
    """

    books = graphene.List(
        BookType,
        description="Retrieve a list of all books."
    )
    book = graphene.Field(
        BookType,
        id=graphene.ID(required=True),
        description="Retrieve a single book."
    )


    def resolve_books(self, info):
        """
        Parameters
        ----------
        info : Any
            Contains useful information and is passed to all resolve methods

        Returns
        -------
        graphene.ObjectType
            A Graphene ObjectType made up of the requested data points.
        """

        books = Book.objects.all()

        return books


    def resolve_book(self, info, id):
        """
        Parameters
        ----------
        info : Any
            Contains useful information and is passed to all resolve methods
        id : str, required
            Author public ID

        Returns
        -------
        graphene.ObjectType
            A Graphene ObjectType made up of the requested data points.
        """

        book = Book.objects.filter(
            public_id=id
        ).first()

        return book


class AuthorMutation(graphene.ObjectType):
    author = AuthorMutation.Field()


class BookMutation(graphene.ObjectType):
    book = BookMutation.Field()
