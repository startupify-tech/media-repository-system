# users/urls.py

from django.conf.urls import url
from django.urls import path
from .views import CreateUserAPIView,SignUpView, UserRetrieveUpdateAPIView,UpdateInterestedTopics
from . import views
urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update/',UserRetrieveUpdateAPIView.as_view()),
    path('interested_topics/', views.UpdateInterestedTopics,name='interested_topics')
]