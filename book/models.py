from django.db import models

# Table for storing book information in the library

class Book(models.Model):
    name = models.CharField(max_length=100)
    publication_address = models.CharField(max_length=50)
    edition = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    publication_date = models.DateField()
    author = models.CharField(max_length=100)


