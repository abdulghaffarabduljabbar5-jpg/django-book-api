from django.urls import path
from rest_framework.routers import DefaultRouter
from API.views import BookLevel2View, BookList , BookDetails , AuthorVS,  BookLevel1View , BookLevel2View , GenereList

router = DefaultRouter()
router.register(r'authors' , AuthorVS , basename='author')

urlpatterns = [
    path('books/' , BookList.as_view() , name='Book-list'),
    path('bookdetail/<int:pk>/' , BookDetails.as_view() , name='Book-Details'),
#urls for the author 
    # path('list' , AuthorVS.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
    # path('detail/<int:pk>/' , AuthorVS.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='author-details'),

    path('books/level1/', BookLevel1View.as_view(), name='book-level1'),
    path('books/level2/', BookLevel2View.as_view(), name='book-level2'),

    path('lists/', GenereList.as_view() , name='genre-list' )
]

urlpatterns +=router.urls