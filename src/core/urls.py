from django.urls import path, re_path

from .views import MediaView

urlpatterns = [
    re_path(r'^media/$', MediaView.as_view(), name='media'),
]
