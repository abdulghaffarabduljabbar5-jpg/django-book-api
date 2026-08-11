from django.shortcuts import render
from API.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API.serializer import BookSerializer
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
