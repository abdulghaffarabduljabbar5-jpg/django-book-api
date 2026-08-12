from rest_framework import serializers
from API.models import Book , Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class BookWithAuthorNameSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(source='author')
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name']

class BookFullNestedSerializer(serializers.ModelSerializer):
    author = AuthorSerializer() 
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
        