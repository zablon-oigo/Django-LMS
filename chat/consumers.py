import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.id=self.scope['url_route']['kwargs']['course_id']
        self.room_group_name=f'chat_{self.id}'
        async_to_sync(self.channel_layer.group_add)(
                        self.room_group_name,
                        self.channel_name
        )

        
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        test_data_json=json.loads(text_data)
        message=test_data_json['message']

        self.send(text_data=json.dumps({'message':message}))