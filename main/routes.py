from django.urls import path
from main import consumer
websocket_routes = [
    path('ws/packaging-task/<str:taskID>/',
         consumer.PackagingTaskProgressConsumer.as_asgi()),
]
