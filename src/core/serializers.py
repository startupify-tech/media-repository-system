from rest_framework import serializers
from .models import Media, Topic
import mimetypes

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()

    class Meta:
        model = Media
        fields = [
            "id", "topic", "title", "file", "mime_type", "description",
            "tags", "author"
        ]

    mime_type = serializers.SerializerMethodField('get_mime_type')
    def get_mime_type(elf, obj):
        return mimetypes.guess_type(obj.file)[0]
