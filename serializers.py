from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'id', 'name', 'books']
        extra_kwargs = {'books': {'view_name': 'book-detail', 'lookup_field': 'pk'}}

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author']
