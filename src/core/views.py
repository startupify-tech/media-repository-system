from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer
from .models import Media,  Topic
from .serializers import MediaSerializer, TopicSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class MediaView(APIView):

    def __get_media_by_topic(self, topic_id):
        topic = get_object_or_404(Topic, pk=topic_id)
        return Media.objects.filter(topic=topic)

    def __get_media_by_subscriber(self, user_id):
        subscriber = get_object_or_404(User, pk=user_id)
        subscriber_interest = subscriber.interested_topic.all()
        media = Media.objects.none()
        for topic in subscriber_interest:
            media |= Media.objects.filter(topic=topic)
        return media

    def get(self, request):
        if 'topic_id' in request.query_params:
            topic_id = request.query_params['topic_id']
            medias = self.__get_media_by_topic(topic_id)
        elif 'user_id' in request.query_params:
            user_id = request.query_params['user_id']
            medias = self.__get_media_by_subscriber(user_id)
        else:
            medias = Media.objects.all()
        serializer = MediaSerializer(medias, many=True)
        return Response(serializer.data)


class TopicView(APIView):

    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)


