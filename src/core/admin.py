from django.contrib import admin

from .models import Media,Topic,Subscriber,Vote

# Register your models here.


admin.site.register(Media)
admin.site.register(Topic)
admin.site.register(Subscriber)
admin.site.register(Vote)