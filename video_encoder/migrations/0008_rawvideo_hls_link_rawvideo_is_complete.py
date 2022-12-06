# Generated by Django 4.1.3 on 2022-11-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_encoder', '0007_alter_rawvideo_name_alter_rawvideo_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawvideo',
            name='hls_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rawvideo',
            name='is_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]