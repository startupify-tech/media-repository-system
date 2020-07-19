# users/urls.py

from django.conf.urls import url
from django.urls import path
from .views import CreateUserAPIView,SignUpView

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    path('signup/', SignUpView.as_view(), name='signup'),

]