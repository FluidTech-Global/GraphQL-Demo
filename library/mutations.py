import graphene
import uuid

from library.models import Author, Book
from library.types import AuthorType, PaginatedAuthorType, BookType


class AuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(
            description="Author public ID (to be passed only when updating an author's details)."
        )
        first_name = graphene.String(
            required=True,
            description="Author's first name."
        )
        last_name = graphene.String(
            required=True,
            description="Author's last name."
        )
        date_of_birth = graphene.String(
            default_value=None,
            required=False,
            description="Author's date of birth."
        )

    author = graphene.Field(AuthorType)


    @classmethod
    def mutate(cls, root, info, id, first_name, last_name, date_of_birth):
        dob = None
        if date_of_birth:
            dob = date_of_birth

        if id:
            query_author = Author.objects.filter(
                public_id=id
            ).first()

            if query_author:
                query_author.first_name = first_name
                query_author.last_name = last_name
                query_author.date_of_birth = dob

                query_author.save()

                return AuthorMutation(author=query_author)
            else:
                raise Exception("Queried author does not exist.")

        else:
            new_author = Author(
                public_id=uuid.uuid4(),
                first_name=first_name,
                last_name=last_name,
                date_of_birth=dob,
            )

            new_author.save()

            return AuthorMutation(author=new_author)


class BookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(
            description="Book public ID (to be passed only when updating a book's details)."
        )
        title = graphene.String(
            required=True,
            description="Book's title."
        )
        author = graphene.String(
            description="Public ID of the book's author"
        )
        isbn = graphene.String(
            required=True,
            description="Book's ISBN."
        )

    book = graphene.Field(BookType)


    @classmethod
    def mutate(cls, root, info, id, title, author, isbn):
        author_obj = None
        if author:
            author_obj = Author.objects.filter(
                public_id=author
            ).first()
        
        if id:
            query_book = Book.objects.filter(
                public_id=id
            ).first()

            if query_book:
                query_book.title = title
                query_book.author = author_obj
                query_book.isbn = isbn

                query_book.save()

                return BookMutation(book=query_book)
            else:
                raise Exception("Queried book does not exist.")

        else:
            new_book = Book(
                public_id=uuid.uuid4(),
                title=title,
                author=author_obj,
                isbn=isbn,
            )

            new_book.save()

            return BookMutation(book=new_book)