import datetime
import sys
import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from celery import shared_task
from video_encoder.utility import generateThumbnail
from video_encoder.models import RawVideo
from main.settings import MEDIA_ROOT
import ffmpeg_streaming
import pathlib


@shared_task(bind=True)
def generateThumbnailTask(self, instance_id, video_file_path):
    imagepath = generateThumbnail(video_file_path)
    RawVideo.objects.filter(id=instance_id).update(
        thumbnail=imagepath.relative_to(MEDIA_ROOT))
    return str(imagepath.relative_to(MEDIA_ROOT))


# Use celery beat to automatically clean up the storage


def CleanUnlinkedVidieos():
    """This function is used to clean the unlinked video files from the storage """
    try:
        linked_files = []
        for object in RawVideo.objects.all():
            linked_file = pathlib.Path(
                object.video_file.url).relative_to('/')
        linked_files.append(linked_file)

        raw_vid_folder = pathlib.Path('media').joinpath('raw_video')
        for sub_folder in raw_vid_folder.iterdir():
            for vid in sub_folder.iterdir():
                if vid in linked_files:
                    pass
                else:
                    print("The unlinked video -->", vid)
                    vid.unlink()
        return 1
    except:
        return 0


def CleanUnlinkedThumbnails():
    """Clean the unlinked thumbnails from the storage"""
    try:
        linked_files = []
        for object in RawVideo.objects.all():
            linked_file = pathlib.Path(
                object.thumbnail.url).relative_to('/')
        linked_files.append(linked_file)

        thumbnails = pathlib.Path('media').joinpath('thumbnail')
        for sub_folder in thumbnails.iterdir():
            for thumbnail in sub_folder.iterdir():
                if thumbnail in linked_files:
                    pass
                else:
                    print("The unlinked thumbnaileo -->", thumbnail)
                    thumbnail.unlink()
        return 1
    except:
        return 0


# @shared_task(bind=True)
# def startPackagingTask(self, id):
#     Controller = startEncoding(id)
#     channel_layer = get_channel_layer()
#     task_id = self.request.id

#     while str(Controller.check_status()) == "ProcessStatus.Running":
#         sleep(10)
#         Controller.check_status()
#         if str(Controller.check_status()) == "ProcessStatus.Finished":
#             async_to_sync(channel_layer.group_send)(
#                 task_id,
#                 {
#                     "type": "celery_task_update",
#                     "data": "TASK COMPLETED",
#                 },
#             )
#             asyncio.set_event_loop_policy(
#                 asyncio.WindowsSelectorEventLoopPolicy())

#             Controller.stop()
#             async_to_sync(channel_layer.group_send)(
#                 task_id,
#                 {
#                     "type": "disconnect",
#                     "data": "TASK FINISHED",
#                 },
#             )

#             break
#     return str("FINAL RETURN STATEMENT")


def monitor(ffmpeg, duration, time_, time_left, process):
    """
    Handling proccess.

    Examples:
    1. Logging or printing ffmpeg command
    logging.info(ffmpeg) or print(ffmpeg)

    2. Handling Process object
    if "something happened":
        process.terminate()

    3. Email someone to inform about the time of finishing process
    if time_left > 3600 and not already_send:  # if it takes more than one hour and you have not emailed them already
        ready_time = time_left + time.time()
        Email.send(
            email='someone@somedomain.com',
            subject='Your video will be ready by %s' % datetime.timedelta(seconds=ready_time),
            message='Your video takes more than %s hour(s) ...' % round(time_left / 3600)
        )
       already_send = True

    4. Create a socket connection and show a progress bar(or other parameters) to your users
    Socket.broadcast(
        address=127.0.0.1
        port=5050
        data={
            percentage = per,
            time_left = datetime.timedelta(seconds=int(time_left))
        }
    )

    :param ffmpeg: ffmpeg command line
    :param duration: duration of the video
    :param time_: current time of transcoded video
    :param time_left: seconds left to finish the video process
    :param process: subprocess object
    :return: None
    """
    # print(ffmpeg)
    # print(duration)
    per = round(time_ / duration * 100)
    sys.stdout.write(
        "\rTranscoding...(%s%%) %s left [%s%s]" %
        (per, datetime.timedelta(seconds=int(time_left)), '#' * per, '-' * (100 - per))
    )
    sys.stdout.flush()


@shared_task(bind=True)
def transcoderTask(self, id):
    print("TRANSCODER STARTED")
    vid_obj = RawVideo.objects.get(id=id)
    vid_url = str(vid_obj.get_video_url).replace('/', '', 1),
    transcoder_vid_input = ffmpeg_streaming.input("videos/emran.mp4")
    hls = transcoder_vid_input.hls(Formats.h264())
    _144p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
    hls.representations(_144p)
    hls.output('media/transcoded/yapri.m3u8', monitor=monitor)
