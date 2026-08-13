# from datetime import date
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from API.models import Book, Author

# class BookList(APITestCase):

#     def setUp(self):
        
#         self.test_author = Author.objects.create(
#             name="Allama Iqbal",
#             date_of_birth=date(1877, 11, 9)
#         )

#         self.book = Book.objects.create(
#             title="Pride and Prejudice",
#             author=self.test_author,
#             published_date="1938-12-11"
#         )
        
#     def test_Book_create(self):
       
#         data = {
#             "title": "The Reconstruction of Religious Thought in Islam",
#             "author": self.test_author.id, 
#             "published_date": "1930-01-01"
#         }

#         response = self.client.post(reverse('Book-list'), data, format='json')
#         # Note: If your endpoint creates items successfully, this status should expect HTTP_201_CREATED
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_Book_get(self):
       
#         response = self.client.get(reverse('Book-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_Book_put(self):
        
#         data = {
#             "title": "Pride and Prejudice Updated",
#             "author": self.test_author.id,
#             "published_date": "1938-12-11"
#         }
        
#         response = self.client.put(reverse('Book-Details', args=(self.book.id,)), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_book_delete(self):

#         response = self.client.delete(reverse('Book-Details', args=(self.book.id,)))
#         self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)


from datetime import date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from API.models import Book, Author , Genre
# 1. IMPORT YOUR SERIALIZERS
from API.serializer import BookSerializer 

class BookSerializerTest(APITestCase):
    """Requirement: Test serialization and deserialization"""

    def setUp(self):
        self.test_author = Author.objects.create(
            name="Allama Iqbal",
            date_of_birth=date(1877, 11, 9)
        )
        self.test_genre = Genre.objects.create(name="History")
        self.book = Book.objects.create(
            title="Bang-e-Dra",
            author=self.test_author,
            published_date=date(1924, 1, 1) # Use date() object, not strings
        )

        self.book.genres.add(self.test_genre)
    def test_serialization(self):
       
        serializer = BookSerializer(instance=self.book)
        data = serializer.data
        
        # Check that the dictionary has the correct data
        self.assertEqual(data['title'], "Bang-e-Dra")
        self.assertEqual(data['author'], self.test_author.id)
        
        self.assertIn('day_since_published', data)
        self.assertIsInstance(data['day_since_published'], int)
        self.assertGreater(data['day_since_published'], 0) 

    def test_deserialization(self):
        
        payload = {
            "title": "New Book",
            "author": self.test_author.id,
            "published_date": "1930-01-01",
            "genres": [self.test_genre.id]
        }
        serializer = BookSerializer(data=payload)
        
        self.assertTrue(serializer.is_valid())
        new_book = serializer.save()
        self.assertEqual(new_book.title, "New Book")
        self.assertIsNotNone(new_book.id)


class BookValidationTest(APITestCase):
    
    def setUp(self):
        self.test_author = Author.objects.create(
            name="Test Author",
            date_of_birth=date(1900, 1, 1)
        )
        self.test_genre = Genre.objects.create(name="Fiction")
    def test_field_level_validation(self):
    
        payload = {
            "title": "AB", # Too short!
            "author": self.test_author.id,
            "published_date": "1930-01-01",
            "genres": [self.test_genre.id]
        }
        serializer = BookSerializer(data=payload)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_object_level_validation(self):
        """Tests your validate() method (assuming you blocked future dates)"""
        future_date = str(date.today().replace(year=date.today().year + 5))
        payload = {
            "title": "Valid Title",
            "author": self.test_author.id,
            "published_date": future_date,
            "genres": [self.test_genre.id]
        }
        serializer = BookSerializer(data=payload)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors) 
      