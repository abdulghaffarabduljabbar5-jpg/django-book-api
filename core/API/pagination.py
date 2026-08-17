from rest_framework.pagination import LimitOffsetPagination , PageNumberPagination

class BookLOPagination(LimitOffsetPagination):
    default_limit = 3

class BookPNPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 5

