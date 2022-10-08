from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, null=True)
    author = models.CharField(blank=True, max_length=200, null=True)
    releaseDate = models.DateField(auto_now=True)


def __str__(self):
    return self.title