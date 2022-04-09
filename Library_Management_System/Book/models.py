from django.db import models

# Create your models here.

class Book_Information(models.Model):
    #book_id = models.IntegerField()
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_cost = models.IntegerField()
    book_quantity = models.IntegerField()
    book_description = models.TextField()

def __str__(self):
    return self.book_title