import graphene

from account.models import User
from account.types import UserType, PaginatedUserType
from graphqldemo.utils import return_paginator


class UserQuery(graphene.ObjectType):
    """
    Defines queries based on the account.models.User model
    """

    users = graphene.List(
        UserType,
        description="Retrieve a list of aLL users."
    )
    paginated_users = graphene.Field(
        PaginatedUserType,
        page=graphene.Int(default_value=1),
        per_page=graphene.Int(default_value=30),
        description="Retrieve a paginated list of users."
    )
    user = graphene.Field(
        UserType,
        id=graphene.ID(required=True),
        description="Retrieve a single user."
    )


    def resolve_users(self, info):
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

        users = User.objects.order_by(
            "first_name"
        ).all()

        return users


    def resolve_paginated_users(self, info, page, per_page):
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

        users = User.objects.order_by(
            "first_name"
        ).all()

        return return_paginator(users, page, per_page, PaginatedUserType)


    def resolve_user(self, info, id):
        """
        Parameters
        ----------
        info : Any
            Contains useful information and is passed to all resolve methods
        id : str, required
            User public ID

        Returns
        -------
        graphene.ObjectType
            A Graphene ObjectType made up of the requested data points.
        """

        user = User.objects.filter(
            public_id=id
        ).first()

        return user