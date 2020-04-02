from django.contrib import admin

from .models import Content

# Register your models here.

def save_model(self, request, obj, form, change):
	if not obj.pk:
		obj.author = request.User.username
	super().save_model(request, obj, form, change)

admin.site.register(Content)