from rest_framework import serializers
from .models import Author, Category, Book, Publisher, Award, Profile, Review, PublisherLocation, BookEdition, Library

# Author Serializer
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = '__all__'
    
    def get_book_count(self, obj):
        return obj.book_set.count()
    
    def get_average_rating(self, obj):
        from django.db.models import Avg
        return obj.book_set.all().aggregate(avg_rating=Avg('review__rating'))['avg_rating']


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Book Serializer
class BasicBookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'author_name', 'publication_date']
# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()
#     Category = CategorySerializer(many=True)

#     class Meta:
#         model = Book
#         fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
#     Category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

#     class Meta:
#         model = Book
#         fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = BasicAuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), 
        source='author', 
        write_only=True
    )
    categories = BasicCategorySerializer(source='Category', many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='Category', 
        many=True, 
        write_only=True
    )
    publisher = BasicPublisherSerializer(read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        source='publisher',
        write_only=True,
        required=False
    )
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()


# Publisher Serializer
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

# Award Serializer
class AwardSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Award
        fields = '__all__'

# Profile Serializers
class ProfileSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Review
        fields = '__all__'

# PublisherLocation Serializer
class PublisherLocationSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = PublisherLocation
        fields = '__all__'

# BookEdition Serializer
class BookEditionSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookEdition
        fields = '__all__'

# Library Serializer
class LibrarySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Library
        fields = '__all__'