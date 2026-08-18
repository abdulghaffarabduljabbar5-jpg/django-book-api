from rest_framework.pagination import LimitOffsetPagination , PageNumberPagination , CursorPagination
from rest_framework.response import Response

class BookLOPagination(LimitOffsetPagination):
    default_limit = 3

class BookPNPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 15

    page_size_query_param = 'size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'page_size': self.get_page_size(self.request),
            "data": data
        })
class BookCPagination(CursorPagination):
    page_size = 4
    page_size_query_param = 'records'
    ordering = '-id'
    
