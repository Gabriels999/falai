import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_name,
            self.room_group_name
        )
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_name,
            self.room_group_name
        )
