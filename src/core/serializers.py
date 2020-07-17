from rest_framework import serializers
from .models import Media, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()

    class Meta:
        model = Media
        fields = '__all__'



