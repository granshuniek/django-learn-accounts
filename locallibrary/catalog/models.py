from django.db import models
from django.core.urlresolvers import reverse

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre.")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, nu;;=True)
    summary = models.TextField(max_length=1000, help_text="Enter a short book description")
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):    
        return reverse('book-detail', kwargs=[str(self.id)])