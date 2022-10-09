from django.db import models
from django.contrib.postgres.fields import ArrayField
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    categories = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8,
    )
    view = models.IntegerField()
    content = RichTextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    categories = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=10,
    )
    synopsis = RichTextField()
    download_url = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.title

class Appointment(models.Model):
    patient = models.CharField(max_length=100)
    hours = models.IntegerField()
    date = models.DateTimeField()
    payed = models.BooleanField()
    transaction_code = models.CharField(max_length=100)

    def __str__(self):
        return self.patient