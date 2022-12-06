from django.db import models
from video_encoder.utility import generateRawVidDir
import ffmpeg


class RawVideoMenager(models.Manager):
    def create(self, **obj_data):
        if obj_data['name'] == None or obj_data['name'] == "":
            obj_data['name'] = str(obj_data['video_file']).split('.')[0]

        return super().create(**obj_data)


class RawVideo(models.Model):
    """User uploaded video files saved in the storage and database"""
    video_file = models.FileField(upload_to=generateRawVidDir)
    name = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="thumbnail", null=True, blank=True)
    hls_link = models.URLField(null=True, blank=True)
    is_complete = models .BooleanField(null=True, blank=True, default=False)
    objects = RawVideoMenager()

    @ property
    def get_video_url(self):
        return self.video_file.url

    @ property
    def get_video_metadata(self):
        return ffmpeg.probe(self.video_file.path)["streams"][0]


class PublishedVideos(models.Model):
    """After packaging the HLS video url and description is saved into this table"""
    raw_video = models.OneToOneField(RawVideo, on_delete=models.CASCADE)
    streaming_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)


class GlobalSettings(models.Model):
    pass
