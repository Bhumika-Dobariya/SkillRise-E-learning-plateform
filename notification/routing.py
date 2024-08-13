

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/notifications/<uuid:student_id>/', consumers.NotificationConsumer.as_asgi()),
]

