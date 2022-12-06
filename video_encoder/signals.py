from django.db.models import signals
from django.dispatch import receiver
from video_encoder.models import RawVideo
from video_encoder.tasks import generateThumbnailTask


@receiver(signals.post_save, sender=RawVideo)
def generate_thumbnail(sender, instance, created, **kwargs):
    video_file_path = instance.video_file.path
    instance_id = instance.id
    generateThumbnailTask.delay(instance_id, video_file_path)
