from django.urls import re_path
from .views import MediaView, TopicView

app_name = 'core'
urlpatterns = [
    re_path(r'^medias/$', MediaView.as_view(), name='medias'),
    re_path(r'^topics/$', TopicView.as_view(), name='topics'),
]
