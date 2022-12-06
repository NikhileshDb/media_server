from django.urls import path

from django.views.generic.base import TemplateView
from video_encoder.views import indexView, uploadNew, singleVideo
from rest_framework import routers
from video_encoder.api_view import RawVideoUploader, PackagerView, CleanUpStorage

urlpatterns = [
    path('template-view/', TemplateView.as_view(template_name="index.html"),),
    path('', indexView, name="index"),
    path('upload-new/', uploadNew, name='upload_new'),
    path('video/<str:pk>', singleVideo, name="single_video"),
    # API VIEW START HERE
    path('api/start-packaging/', PackagerView.as_view(), name="start_packaging"),
    path('api/unlinked-files/', CleanUpStorage.as_view())
]


router = routers.SimpleRouter()
router.register('api/upload-new', RawVideoUploader)

urlpatterns += router.urls
