from django.shortcuts import render, get_object_or_404
from .models import Media, Subscriber, Topic
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import MediaSerializer


# Create your views here.

# def home_view(request, *args, **kwargs):
#     return render(request, "home.html", {})


class MediaView(APIView):
    def __get_media_by_topic(self, topic_id):
        get_object_or_404(Topic, pk=topic_id)
        return Media.objects.filter(topic=topic_id)

    def __get_media_by_subscriber(self, user_id):
        subscriber = get_object_or_404(Subscriber, pk=user_id)
        subscriber_interest = subscriber.interested_topic.all()
        media = Media.objects.none()
        for topic in subscriber_interest:
            media |= Media.objects.filter(topic=topic)
        return media

    # try&except for both user_id and topic_id
    def validation_check(self, value):
        # try&except is necessary because if topic_id=asd or some character other than integer get_or_404() throws
        # an error(value error).
        try:
            num = int(value)  # parses query parameter(strings) that is topic_id into integer.
            if num < 0:  # condition can be either num<=0 or num<0.
                raise ValueError
        except ValueError:
            return False
        else:
            return True

    def get(self, request):
        if 'topic_id' in request.query_params:
            topic_id = request.query_params['topic_id']
            if self.validation_check(topic_id):
                media = self.__get_media_by_topic(topic_id)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif 'user_id' in request.query_params:
            user_id = request.query_params['user_id']
            if self.validation_check(user_id):
                media = self.__get_media_by_subscriber(user_id)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data)
