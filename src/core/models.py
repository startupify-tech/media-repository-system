

from django.db import models

from django.contrib.auth.models import User
from .utility import get_file_path

# from django.contrib.postgres.fields import ArrayField


P = "PREMIUM"
F = "FREE"

TYPE_CHOICES = (
    (P, "Premium"),
    (F, "Free"),
)
NIL = "nil"


# Create your models here.

class Topic(models.Model):
    Name = models.CharField(max_length=30, null=True)


class Media(models.Model):
    Title = models.CharField(max_length=30, null=True)
    Description = models.TextField(null=True)
    File = models.FileField(upload_to=get_file_path, null=True, blank=True, max_length=255)
    Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)

    Tags = models.CharField(max_length=20, null=True, blank=True)



class Subscriber(models.Model):
    First = models.CharField(max_length=30, null=True)
    Last = models.CharField(max_length=30, null=True, blank=True)
    Email = models.EmailField()
    Type = models.CharField(max_length=30,
                            choices=TYPE_CHOICES,
                            default=F)
    Interest = models.CharField(max_length=30, null=True)


class Vote(models.Model):
    Voted_by = models.ForeignKey(Subscriber, on_delete=models.SET_NULL, null=True, blank=True)
    Voted_for = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
