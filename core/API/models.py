from django.db import models

#create the author model for that
class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50 , unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author , on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField(Genre , related_name='genre')
    published_date = models.DateField()

    def __str__(self):
        return self.title


    