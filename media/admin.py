from django.contrib import admin
from .models import media
from .models import topic,subscriber,vote
# Register your models here.

admin.site.register(topic)
admin.site.register(subscriber)
admin.site.register(vote)     
admin.site.register(media)