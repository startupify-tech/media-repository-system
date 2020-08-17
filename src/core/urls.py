from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import MediaView, TopicView

app_name = 'core'
urlpatterns = [
    re_path(r'^medias/$', MediaView.as_view(), name='medias'),
    re_path(r'^topics/$', TopicView.as_view(), name='topics'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
