from rest_framework.pagination import LimitOffsetPagination

class BookLOPagination(LimitOffsetPagination):
    default_limit = 3

