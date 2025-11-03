from django.urls import path
from .views import socket_test_view

urlpatterns = [
    path('socket-test/', socket_test_view, name='socket_test'),
]
