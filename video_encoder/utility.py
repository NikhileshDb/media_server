from datetime import date
import ffmpeg
from pathlib import Path
from main.settings import MEDIA_ROOT


def generateRawVidDir(instance, filename):
    return "raw_video/{0}/{1}".format(date.today(), filename.lower())


def generateOutPutLocation(filename):
    return "encoded_files/{0}/{1}".format(date.today(), filename.lower())


def generateThumbnail(in_filename):
    """Takes the video filepath and generates a thumbnail in the media/thumbnail/directory"""
    probe = ffmpeg.probe(in_filename)
    time = float(probe['streams'][0]['duration']) // 2
    width = probe['streams'][0]['width']
    thumb_folder = Path(MEDIA_ROOT).joinpath('thumbnail')
    if not thumb_folder.exists():
        thumb_folder.mkdir()
    out_filename = thumb_folder.joinpath(
        "{}.jpg".format(Path(in_filename).stem))
    if not out_filename.exists():
        out_filename.touch()
    try:
        (ffmpeg.input(in_filename, ss=time).filter(
            'scale', width, -1).output("{}".format(out_filename), vframes=1).overwrite_output().run())
        # save the image object in the database
        return out_filename
    except ffmpeg.Error as e:
        return None
