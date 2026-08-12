from django.urls import path
from API.views import BookLevel2View, BookList , BookDetails , AuthorList , AuthorDetails ,  BookLevel1View , BookLevel2View

urlpatterns = [
    path('books/' , BookList.as_view() , name='Book-list'),
    path('bookdetail/<int:pk>/' , BookDetails.as_view() , name='Book-Details'),
#urls for the author 
    path('list' , AuthorList.as_view(), name='author-list'),
    path('detail/<int:pk>/' , AuthorDetails.as_view(), name='author-details'),

    path('books/level1/', BookLevel1View.as_view(), name='book-level1'),
    path('books/level2/', BookLevel2View.as_view(), name='book-level2'),

]