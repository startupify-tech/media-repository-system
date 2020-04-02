from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
	title       = models.CharField(max_length=20)
	description = models.TextField()
	author      = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)
	file        = models.FileField(upload_to='uploads/%Y/%m/%d',blank=True)