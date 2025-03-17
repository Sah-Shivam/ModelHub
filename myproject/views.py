from rest_framework import viewsets
from .models import Author, Category, Book, Publisher, Award, Profile, Review, PublisherLocation, BookEdition, Library
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, PublisherSerializer, AwardSerializer, ProfileSerializer, ReviewSerializer, PublisherLocationSerializer, BookEditionSerializer, LibrarySerializer

# Author ViewSet
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Book ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Publisher ViewSet
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

# Award ViewSet
class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

# Profile ViewSet
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# PublisherLocation ViewSet
class PublisherLocationViewSet(viewsets.ModelViewSet):
    queryset = PublisherLocation.objects.all()
    serializer_class = PublisherLocationSerializer

# BookEdition ViewSet
class BookEditionViewSet(viewsets.ModelViewSet):
    queryset = BookEdition.objects.all()
    serializer_class = BookEditionSerializer

# Library ViewSet
class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer