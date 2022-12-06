from django.apps import AppConfig


class VideoEncoderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video_encoder'

    def ready(self):
        import video_encoder.signals
