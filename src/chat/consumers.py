import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from . models import RoomMember

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        member, created = RoomMember.objects.get_or_create(
            user=self.scope["user"],
            room_name = self.scope["url_route"]["kwargs"]["room_name"]
        )

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):

        member = RoomMember.objects.get(
            user = self.scope["user"],
            room_name = self.scope["url_route"]["kwargs"]["room_name"]
        )
        member.delete()
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
           
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, "sender":sender}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        print("self.request.user = ", self.scope["user"].username)
        print("sender type = ", event["sender"])
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message,"sender": event["sender"], }))