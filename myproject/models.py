from django.db import models


#main models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Category(models.Model):
    title = models.CharField(max_length=100)

class Book(models.Model):  # First level foregin relation key 
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)      #one to Many
    Category = models.ManyToManyField(Category)   # Many to Many 


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)


class Award(models.Model):
    award_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    # Many-to-Many Relationship with Author
    authors = models.ManyToManyField(Author)



# Foreign Key Models
class Profile(models.Model):
    author = models.OneToOneField(Author,on_delete=models.CASCADE)  
    bio = models.TextField() 


class Review(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()


class PublisherLocation(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # One-to-Many
    city = models.CharField(max_length=100)




# Second Level Foreign Key Models
class BookEdition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    edition_number = models.IntegerField()
    published_date = models.DateField()
  

class Library(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)