from django.shortcuts import render
from API.models import Book , Author , Genre
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view 
from rest_framework import viewsets
from API.serializer import BookSerializer , AuthorSerializer , BookFullNestedSerializer, BookWithAuthorNameSerializer , GenreSerializer , AuthorHyperlinkedSerializer
from rest_framework import generics
# Create your views here.

# @api_view(['GET' , 'POST'])
# def BookList(request):
#     if request.method == 'GET':
#         book = Book.objects.all()
#         serializer = BookSerializer(book , many=True)
#         return Response({'Books': serializer.data})

#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Book is created": serializer.data})
#         return Response(serializer.errors)

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title' , 'author']

    filter_backends = [SearchFilter]
    search_fields = ['title', 'author__name']

class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Now we will use the another method that is viewset method 

# class AuthorVS(viewsets.ViewSet):
#     def list(self , request):
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset , many=True , context = {'request': request} )
#         return Response(serializer.data)
#     def create(self , request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request , pk=None):
#         queryset = Author.objects.all()
#         author = get_object_or_404(queryset , pk=pk)
#         serializer = AuthorSerializer(author ,context = {'request': request} )
#         return Response(serializer.data)

#     def update(self,  request , pk=None):
#         queryset = Author.objects.all()
#         author = get_object_or_404(queryset , pk=pk)
#         serializer = AuthorSerializer(author , context = {'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request , pk=None):
#         queryset = Author.objects.all()
#         author = get_object_or_404(queryset , pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True , methods=['get'])
    def stats(self , request , pk=None):
        author = self.get_object()
        return Response({"words": 50000 , "days_old": 1000})
        
# Now we will use the second method that is viewset method
class AuthorLCU(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True , methods=['get'])
    def stats(self , request , pk=None):
        author = self.get_object()
        return Response({"words": 50000 , "days_old": 1000})
    

# #serializer for the author list and detail
# class AuthorList(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     # serializer_class = AuthorSerializer
#     serializer_class = AuthorHyperlinkedSerializer

# class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     # serializer_class = AuthorSerializer
#     serializer_class = AuthorHyperlinkedSerializer

class BookLevel1View(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookWithAuthorNameSerializer

class BookLevel2View(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class =  BookFullNestedSerializer

class GenereList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    