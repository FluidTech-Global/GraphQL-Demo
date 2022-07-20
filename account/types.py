import graphene

from graphene_django import DjangoObjectType

from account.models import User
from graphqldemo.utils import PaginatedObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = [
            "public_id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class PaginatedUserType(PaginatedObjectType):
    """
    Defines a paginated UserType
    """

    objects = graphene.List(
        UserType,
        description="List of users (UserType)"
    )