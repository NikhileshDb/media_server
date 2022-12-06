# from video_encoder.tasks import start_new_hit_job


# for i in range(100):
#     start_new_hit_job("sdasd")

# celery flower --basic_auth=user1:pass123 --port=5555 --broker=redis://localhost:6379/0
# celery --broker=redis://localhost:6379/0 flower --port=5555 --broker=redis://localhost:6379/0
# celery -A main worker -l info --concurrency=5
# celery -A main worker --pool=eventlet -l info
# celery -A main worker --pool=solo -l info
# celery -A main --broker=redis://localhost:6379/0 flower --port=5999

# {
#     'index': 0,
#     'codec_name': 'h264',
#     'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10',
#     'profile': 'Main',
#     'codec_type': 'video',
#     'codec_tag_string': 'avc1',
#     'codec_tag': '0x31637661',
#     'width': 1280,
#     'height': 676,
#     'coded_width': 1280,
#     'coded_height': 676,
#     'closed_captions': 0,
#     'film_grain': 0,
#     'has_b_frames': 1,
#     'sample_aspect_ratio': '1:1',
#     'display_aspect_ratio': '320:169',
#     'pix_fmt': 'yuv420p',
#     'level': 31,
#     'color_range': 'tv',
#     'color_space': 'bt709',
#     'color_transfer': 'bt709',
#     'color_primaries': 'bt709',
#     'chroma_location': 'left',
#     'field_order': 'progressive',
#     'refs': 1,
#     'is_avc': 'true',
#     'nal_length_size': '4',
#     'id': '0x1',
#     'r_frame_rate': '24/1',
#     'avg_frame_rate': '24/1',
#     'time_base': '1/12288',
#     'start_pts': 0,
#     'start_time': '0.000000',
#     'duration_ts': 3660800,
#     'duration': '297.916667',
#     'bit_rate': '545326',
#     'bits_per_raw_sample': '8',
#     'nb_frames': '7150',
#     'extradata_size': 44,
#     'disposition': {
#         'default': 1,
#         'dub': 0,
#         'original': 0,
#         'comment': 0,
#         'lyrics': 0,
#         'karaoke': 0,
#         'forced': 0,
#         'hearing_impaired': 0,
#         'visual_impaired': 0,
#         'clean_effects': 0,
#         'attached_pic': 0,
#         'timed_thumbnails': 0,
#         'captions': 0,
#         'descriptions': 0,
#         'metadata': 0,
#         'dependent': 0,
#         'still_image': 0},
#     'tags': {
#         'language':
#             'und',
#             'handler_name': 'ISO Media file produced by Google Inc.',
#             'vendor_id': '[0][0][0][0]'
#     }}
