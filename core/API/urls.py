from django.urls import path
from API.views import BookLevel2View, BookList , BookDetails , AuthorLCU,  BookLevel1View , BookLevel2View , GenereList

urlpatterns = [
    path('books/' , BookList.as_view() , name='Book-list'),
    path('bookdetail/<int:pk>/' , BookDetails.as_view() , name='Book-Details'),
#urls for the author 
    path('list' , AuthorLCU.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
    path('detail/<int:pk>/' , AuthorLCU.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy' , 'patch': 'partial_update'}), name='author-details'),

    path('books/level1/', BookLevel1View.as_view(), name='book-level1'),
    path('books/level2/', BookLevel2View.as_view(), name='book-level2'),

    path('lists/', GenereList.as_view() , name='genre-list' )
]