from django.contrib import admin

from .models import Media, Topic, Vote

# Register your models here.


admin.site.register(Media)
admin.site.register(Topic)
# @admin.register(Subscriber)
# class SubscriberAdmin(admin.ModelAdmin):
#    list_display = ('first','last', 'email', 'type')
admin.site.register(Vote)
