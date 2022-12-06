from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class PackagingTaskProgressConsumer(WebsocketConsumer):
    def celery_task_update(self, event):
        self.send(text_data=event["data"])

    def connect(self):
        self.accept()
        taskID = self.scope.get("url_route").get("kwargs").get("taskID")
        async_to_sync(self.channel_layer.group_add)(taskID, self.channel_name)
        print("Yeah Connected Ok")
        print(self.channel_layer)

    def disconnect(self, close_code):
        taskID = self.scope.get("url_route").get("kwargs").get("taskID")
        async_to_sync(self.channel_layer.group_discard)(
            taskID, self.channel_name)
        print("YEAH DISCONNECTED FROM THE CLIENT")
        self.close()

    def receive(self, text_data):
        print(text_data)
        print(self.channel_layer)
