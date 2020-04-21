from rest_framework import serializers
from .models import topic

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model=topic
		fields=['Name']
		
		

