from rest_framework import serializers
from .models import Author, Category, Book, Publisher, Award, Profile, Review, PublisherLocation, BookEdition, Library

# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    Category = CategorySerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
#     Category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

#     class Meta:
#         model = Book
#         fields = '__all__'


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