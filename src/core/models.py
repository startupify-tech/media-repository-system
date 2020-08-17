from django.db import models
from django.contrib.auth.models import User
from .utility import get_file_path
from django.conf import settings


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Media(models.Model):
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)
    _file = models.FileField(upload_to=get_file_path, null=True, blank=True, max_length=255)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, db_column="name", on_delete=models.SET_NULL, null=True, blank=True)

    tags = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def file(self):
        return (settings.DOMAIN_NAME + self._file.name)


class Subscriber(models.Model):
    P = "PREMIUM"
    F = "FREE"

    TYPE_CHOICES = (
        (P, "Premium"),
        (F, "Free"),
    )

    first = models.CharField(max_length=30, null=True)
    last = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    type = models.CharField(max_length=30,
                            choices=TYPE_CHOICES,
                            default=F)
    interested_topic = models.ManyToManyField(Topic)

    def __str__(self):
        return str(self.first)


class Vote(models.Model):
    voted_by = models.ForeignKey(Subscriber, on_delete=models.SET_NULL, null=True, blank=True)
    voted_for = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

