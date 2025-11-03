import os
import socketio
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatserver.settings')

sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*',  # allow all origins (adjust for production)
    ping_interval=25,  # send a ping every 25 seconds
    ping_timeout=60    # disconnect if no pong received within 60s
)

# Django ASGI app
django_app = get_asgi_application()

# Import socket event handlers so they get registered
import chat.sockets

# Combine Django + Socket.IO
application = socketio.ASGIApp(sio, django_app)
