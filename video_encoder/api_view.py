from video_encoder.serilaizers import RawVideoSerializer, PackagingSerializer
from rest_framework import viewsets
from video_encoder.models import RawVideo
from rest_framework.response import Response
from video_encoder.tasks import transcoderTask
from rest_framework.views import APIView
from rest_framework import status
import pathlib


class PackagerView(APIView):
    serializer_class = PackagingSerializer

    def post(self, request):
        id = request.data.get('object_id')
        task_id = transcoderTask.delay(id)
        print(task_id)
        return Response(
            data={"task_id": task_id.id},
            status=status.HTTP_200_OK,
        )

    def get(self, request, **kwargs):
        return Response(data={"message": "Post id to start packaging task"},
                        status=status.HTTP_200_OK,)


class RawVideoUploader(viewsets.ModelViewSet):
    queryset = RawVideo.objects.all()
    serializer_class = RawVideoSerializer


class CleanUpStorage(APIView):
    def get(self, request, **kwargs):

        return Response(data={"message": "Post id to start packaging task"},
                        status=status.HTTP_200_OK,)

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
