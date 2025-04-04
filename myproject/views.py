from rest_framework import viewsets,filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author, Category, Book, Publisher, Award, Profile, Review, PublisherLocation, BookEdition, Library
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, PublisherSerializer, AwardSerializer, ProfileSerializer, ReviewSerializer, PublisherLocationSerializer, BookEditionSerializer, LibrarySerializer

# Author ViewSet

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nationality', 'birth_date']
    search_fields = ['name', 'bio']
    ordering_fields = ['name', 'birth_date']

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        author = self.get_object()
        books = Book.objects.filter(author=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def top_authors(self, request):
        authors = Author.objects.annotate(book_count=Count('book')).order_by('-book_count')[:10]
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)   

# Category ViewSet
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    
    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        category = self.get_object()
        books = Book.objects.filter(Category=category)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

# Book ViewSet
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer





class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'Category', 'publication_date', 'isbn']
    search_fields = ['title', 'isbn', 'author__name']
    ordering_fields = ['title', 'publication_date', 'price']
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        book = self.get_object()
        reviews = Review.objects.filter(book=book)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_books = Book.objects.all().order_by('-publication_date')[:5]
        serializer = BookSerializer(recent_books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        top_books = Book.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')[:10]
        serializer = BookSerializer(top_books, many=True)
        return Response(serializer.data)

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