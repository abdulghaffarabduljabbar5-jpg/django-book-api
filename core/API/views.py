from django.shortcuts import render
from API.models import Book , Author , Genre
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#serializer for the author list and detail
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    # serializer_class = AuthorSerializer
    serializer_class = AuthorHyperlinkedSerializer

class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    # serializer_class = AuthorSerializer
    serializer_class = AuthorHyperlinkedSerializer

class BookLevel1View(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookWithAuthorNameSerializer

class BookLevel2View(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class =  BookFullNestedSerializer

class GenereList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer