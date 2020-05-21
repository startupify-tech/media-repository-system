from django.urls import path, re_path

from .views import MediaView, TopicView

urlpatterns = [
    re_path(r'^media/$', MediaView.as_view(), name='media'),
    re_path(r'^topic$', TopicView.as_view(), name='topic'),
]
