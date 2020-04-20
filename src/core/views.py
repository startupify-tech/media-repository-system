from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Media, Topic
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
        qs = Media.objects.filter(Topic=1)
        serializer = MediaSerializer(qs, many=True)
        return Response(serializer.data)