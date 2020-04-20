from django.db import models
from django.contrib.auth.models import User
from .utility import get_file_path


# Create your models here.

class Topic(models.Model):
    Name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.Name


class Media(models.Model):
    Title = models.CharField(max_length=30, null=True)
    Description = models.TextField(null=True)
    File = models.FileField(upload_to=get_file_path, null=True, blank=True, max_length=255)

    Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Topic = models.ForeignKey(Topic, db_column="Name", on_delete=models.SET_NULL, null=True, blank=True)

    Tags = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Title


class Subscriber(models.Model):
    P = "PREMIUM"
    F = "FREE"

    TYPE_CHOICES = (
        (P, "Premium"),
        (F, "Free"),
    )

    First = models.CharField(max_length=30, null=True)
    Last = models.CharField(max_length=30, null=True, blank=True)
    Email = models.EmailField()
    Type = models.CharField(max_length=30,
                            choices=TYPE_CHOICES,
                            default=F)
    Interest = models.ManyToManyField(Topic)

    def __str__(self):
        return str(self.First + " " + self.Last)


class Vote(models.Model):
    Voted_by = models.ForeignKey(Subscriber, on_delete=models.SET_NULL, null=True, blank=True)
    Voted_for = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
