from django.urls import path
from API.views import BookList , BookDetails , AuthorList , AuthorDetails

urlpatterns = [
    path('book/' , BookList.as_view() , name='Book-list'),
    path('bookdetail/<int:pk>/' , BookDetails.as_view() , name='Book-Details'),
    path('list' , AuthorList.as_view(), name='author-list'),
    path('detail/<int:pk>/' , AuthorDetails.as_view(), name='author-details')
]