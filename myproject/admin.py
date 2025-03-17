from django.contrib import admin
from .models import Author, Category, Book, Publisher, PublisherLocation, Profile

# Register your models here.

from .models import (
    Author, Category, Book, Publisher, 
    Profile, Review, PublisherLocation, 
    BookEdition, Award, Library
)

admin.site.register([Author, Category, Book, Publisher, 
                     Profile, Review, PublisherLocation, 
                     BookEdition, Award, Library])