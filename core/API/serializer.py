from rest_framework import serializers
from API.models import Book , Author , Genre
from datetime import datetime , date
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add your custom user data fields into the JWT payload
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class BookSerializer(serializers.ModelSerializer):
    day_since_published = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self,value):
        if len(value) < 3:
            raise serializers.ValidationError("Name should be almost 3 characters")
        return value


    def validate(self, attrs):
        """Object-level validation: ensure published_date is not in the future."""
        published_date = attrs.get('published_date')
        if published_date and published_date > date.today():
            raise serializers.ValidationError({
                "non_field_errors": ["Cannot be a future date"]
            })
        return attrs

    def get_day_since_published(self, obj):
        """Return number of days since the book was published (int)."""
        published_date = getattr(obj, 'published_date', None)
        if not published_date:
            return 0
        delta = date.today() - published_date
        return delta.days
   
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def validate_date(self, attr):
        published_date = attr.get('published-date')
        if published_date and published_date > date.today():
            raise serializers.ValidationError("Date should not be future a future date" )
            
class AuthorNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name should be at least 3 characters long")

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

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class AuthorHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Author
            fields = ['url' , 'name' , 'bio' , 'date_of_birth']

            extra_kwargs={
                'url': {'view_name': 'author-details'}
            }
        