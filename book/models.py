from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    publication_address = models.CharField(max_length=50)
    edition = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    publication_date = models.DateField()

class Author(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


