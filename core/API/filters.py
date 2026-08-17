import django_filters
from rest_framework.filters import BaseFilterBackend
from .models import Book

class BookFilterSet(django_filters.FilterSet):
    published_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ['published_date']

class ComplexLogicFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        user = request.user

        if user.is_anonymous:
            if hasattr(Book , 'status'):
                return queryset.filter(status='published')

        return queryset
