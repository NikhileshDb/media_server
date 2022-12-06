# import pathlib
# from main.settings import MEDIA_ROOT
# from streamer import controller_node

# from video_encoder.models import RawVideo
# ENCODER_CONTROLLER = controller_node.ControllerNode()


# def startEncoding(id):
#     video = RawVideo.objects.get(id=id)
#     if pathlib.Path.joinpath(MEDIA_ROOT, 'packaged').exists():
#         pass
#     else:
#         pathlib.Path.joinpath(MEDIA_ROOT, 'packaged').mkdir(exist_ok=True)
#     try:
#         ENCODER_CONTROLLER.start(
#             output_location="{0}/packaged/{1}".format(MEDIA_ROOT,
#                                                       str(video.name).replace(' ', "_")),
#             input_config_dict=dict({
#                 "inputs": [
#                     {
#                         "input_type": "file",
#                         "name": str(video.get_video_url).replace('/', '', 1),
#                         "media_type": "video",
#                     },
#                     {
#                         "input_type": "file",
#                         "name":  str(video.get_video_url).replace('/', '', 1),
#                         "media_type": 'audio',
#                     }
#                 ]}),
#             pipeline_config_dict={"streaming_mode": "vod", "resolutions": ['720p'],
#                                   'channel_layouts': ['stereo'],
#                                   'video_codecs': ['h264'],
#                                   'audio_codecs': ['aac'],
#                                   'manifest_format': ['hls'],
#                                   'segment_size': 10,
#                                   'segment_per_file': True,
#                                   'hls_output': str(video.name + ".m3u8").replace(' ', '_'),
#                                   },
#             use_hermetic=True,
#         )
#         return ENCODER_CONTROLLER
#     except Exception as e:
#         print(e)
