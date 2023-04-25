from django.urls import path

from rooms import consumers

websocket_urlpatterns = [
    path('ws/<str:room_slug>/', consumers.ChatConsumer.as_asgi()),
]
