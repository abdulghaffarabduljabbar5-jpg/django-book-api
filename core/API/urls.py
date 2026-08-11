from django.urls import path
from API.views import BookList

urlpatterns = [
    path('book/' , BookList , name='Book-list')
]