from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import topic
from .serializers import PostSerializer

class GetTopics(APIView):
	def get(self,request,*args,**kwargs):
		t   =topic.objects.all()
		serializer = PostSerializer(t, many=True)
		return Response(serializer.data)
