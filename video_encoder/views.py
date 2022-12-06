import json
from django.shortcuts import render, redirect
from video_encoder.models import RawVideo


def indexView(request):
    uploaded_videos = RawVideo.objects.all()
    context = {
        'videos': uploaded_videos
    }
    return render(request, 'index.html', context)


def check_status(request):
    return render(request, 'index.html')


def singleVideo(request, pk):
    video = RawVideo.objects.get(pk=pk)
    metadata = json.dumps(video.get_video_metadata, indent=4)
    context = {
        'video': video,
        'metadata': metadata
    }
    return render(request, 'single_video.html', context)


def uploadNew(request):
    if request.method == 'POST':
        try:
            video_file = request.FILES.get('video')
            instanceObject = RawVideo.objects.create_video(
                video_file=video_file, name=None)
            instanceObject.save()
            return redirect('index')
        except Exception as e:
            print(e)
    return render(request, 'upload_new.html')
