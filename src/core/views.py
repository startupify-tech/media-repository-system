from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Media, Topic, Subscriber
from django.shortcuts import render

from .serializers import MediaSerializer, TopicSerializer


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


class MediaView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Media.objects.all()
        serializer = MediaSerializer(qs, many=True)
        return Response(serializer.data)


class TopicView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Topic.objects.all()
        serializer = TopicSerializer(qs, many=True)
        return Response(serializer.data)


class TopicMediaView(APIView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.GET:
            qs = Media.objects.filter(Topic=request.GET['id'])
        else:
            qs = Media.objects.filter(Topic=1)
        serializer = MediaSerializer(qs, many=True)
        return Response(serializer.data)


class SubscriberMediaView(APIView):
    def get(self, request, *args, **kwargs):
        # if the user doesnot gives an id of the subscriber
        # then the api gives default result for id=1
        if 'id' in request.GET:
            subscribers = Subscriber.objects.filter(id=request.GET['id'])
        else:
            subscribers = Subscriber.objects.filter(id=1)

        qs = Media.objects.none()  # initializing  empty query set

        # for each subscriber getting a list of topics they are interested in and then adding
        # topic to the query set ( qs )
        for s in subscribers:
            topics_of_interest_of_subscriber = s.Interest.all()
            for topic in topics_of_interest_of_subscriber:
                qs |= Media.objects.filter(Topic=topic)
        serializer = MediaSerializer(qs, many=True)
        return Response(serializer.data)
