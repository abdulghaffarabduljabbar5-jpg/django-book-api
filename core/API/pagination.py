from rest_framework.pagination import LimitOffsetPagination , PageNumberPagination , CursorPagination

class BookLOPagination(LimitOffsetPagination):
    default_limit = 3

class BookPNPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 5

class BookCPagination(CursorPagination):
    page_size = 4
    page_size_query_param = 3
    ordering = '-id'
    
