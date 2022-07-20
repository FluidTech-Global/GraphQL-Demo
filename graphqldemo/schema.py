import graphene

from account.schema import UserQuery
from library.schema import AuthorQuery, BookQuery
from library.schema import AuthorMutation, BookMutation


class ApiQuery(
    UserQuery,
    AuthorQuery,
    BookQuery
):
    pass


class ApiMutation(
    AuthorMutation,
    BookMutation
):
    pass


api_schema = graphene.Schema(query=ApiQuery, mutation=ApiMutation)
