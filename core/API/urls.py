from django.urls import path
from API.views import BookList , BookDetails

urlpatterns = [
    path('book/' , BookList.as_view() , name='Book-list'),
    path('bookdetail/<int:pk>/' , BookDetails.as_view() , name='Book-Details')
]