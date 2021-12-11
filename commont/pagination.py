from django.core import paginator
from django.core.paginator import InvalidPage
from rest_framework import pagination
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'perpage'


    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['current'] = self.page.number
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response

#img select
# keyword
