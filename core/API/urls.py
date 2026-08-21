from rest_framework.routers import DefaultRouter
from API.views import (
    BookLevel2View, 
    BookList , 
    BookDetails , 
    AuthorLCU,  
    BookLevel1View , 
    GenereList)
from rest_framework.authtoken import views as drf_token_views
from API.views import ValidateTokenView
from django.urls import include , path
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'authors' , AuthorLCU , basename='author')

urlpatterns = [
    path('books/' , BookList.as_view() , name='Book-list'),
    path('bookdetail/<int:pk>/' , BookDetails.as_view() , name='Book-Details'),
#urls for the author 
    # path('list' , AuthorVS.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
    # path('detail/<int:pk>/' , AuthorVS.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='author-details'),

    path('books/level1/', BookLevel1View.as_view(), name='book-level1'),
    path('books/level2/', BookLevel2View.as_view(), name='book-level2'),

    path('lists/', GenereList.as_view() , name='genre-list' ),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/generate/', drf_token_views.obtain_auth_token),
    path('token/validate/', ValidateTokenView.as_view()),

    path('auth/' , include('rest_framework.urls'))
]

urlpatterns +=router.urls