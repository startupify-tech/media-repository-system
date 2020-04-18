from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Media

from .serializers import MediaSerializer


# Create your views here.

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Media.objects.all()
        serializer = MediaSerializer(qs, many=True)
        return Response(serializer.data)
