from rest_framework import serializers
from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

    topic_name = serializers.SerializerMethodField('get_topic_name')

    def get_topic_name(self, obj):
        return obj.topic.name
