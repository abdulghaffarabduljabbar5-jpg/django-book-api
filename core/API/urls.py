from django.urls import path
from API.views import BookList

urlpatterns = [
    path('book/' , BookList.as_view() , name='Book-list')
]