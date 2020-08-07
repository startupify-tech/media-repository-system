from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from .utility import get_file_path
from django.contrib.auth import get_user_model
User = get_user_model()


class Topic(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Media(LoginRequiredMixin, models.Model):
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)
    file = models.FileField(upload_to=get_file_path, null=True, blank=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, db_column="name", on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    paginate_by = 10

    def __str__(self):
        return self.title


class Vote(models.Model):
    voted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    voted_for = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
