import graphene

from django.db.models.query import QuerySet
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from typing import Any


def return_paginator(queryset: QuerySet, page: int, per_page: int, paginated_graphql_type: Any, **kwargs) -> tuple:
    """
    Helper function that provides for an easy implementation of pagination using built-in Django pagination functions.
    Inspired by: https://gist.github.com/Khongchai/a8c90b6735474d33e13ccb9b98c7c32f
    
    Parameters
    ----------
    queryset : django.db.models.query.QuerySet, required
        A Django queryset.
    page : int, required
        The desired page number. Set to 0 to fetch all records.
    per_page : int, required
        The number of items to show per page.
    paginated_graphql_type: graphene.ObjectType, required
        The desired paginated GraphQL object.

    Returns
    -------
    tuple
        A tuple made up of
            - the current page
            - the number of pages
            - has next page
            - has previous page
            - total number of objects in the queryset
            - objects
    """

    pagination_obj = Paginator(queryset, per_page)

    try:
        page_obj = pagination_obj.page(page)
    except PageNotAnInteger:
        # Should the page parameter passed not be an integer, fetch the first page
        page_obj = pagination_obj.page(1)
    except EmptyPage:
        # Should the fetched page be empty, fetch the last page (num_pages)
        page_obj = pagination_obj.page(pagination_obj.num_pages)
    
    if page == 0:
        return paginated_graphql_type(
            page = 1,
            pages = 1,
            total = queryset.count(),
            next_page = None,
            previous_page = None,
            has_next = False,
            has_previous = False,
            objects = queryset,
            **kwargs
        )
    
    else:
        return paginated_graphql_type(
            page = page_obj.number,
            pages = pagination_obj.num_pages,
            total = queryset.count(),
            next_page = page_obj.number + 1 if page_obj.has_next() else None,
            previous_page = page_obj.number - 1 if page_obj.has_previous() else None,
            has_next = page_obj.has_next(),
            has_previous = page_obj.has_previous(),
            objects = page_obj.object_list,
            **kwargs
        )


class PaginatedObjectType(graphene.ObjectType):
    """
    Custom object type that adds provision for pagination.
    """

    page = graphene.Int(
        description="The current page number. Set to 0 to view all records."
    )
    pages = graphene.Int(
        description="The number of pages."
    )
    total = graphene.Int(
        description="The total number of items."
    )
    next_page = graphene.Int(
        description="The next page number."
    )
    previous_page = graphene.Int(
        description="The previous page number."
    )
    has_next = graphene.Boolean(
        description="Boolean indicating whether a next page exists."
    )
    has_previous = graphene.Boolean(
        description="Boolean indicating whether a previous page exists."
    )