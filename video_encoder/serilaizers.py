from rest_framework.serializers import ModelSerializer, Serializer, IntegerField
from video_encoder.models import RawVideo


class RawVideoSerializer(ModelSerializer):
    class Meta:
        model = RawVideo
        fields = '__all__'


class PackagingSerializer(Serializer):
    object_id = IntegerField()

    class Meta:
        fileds = '__all__'
