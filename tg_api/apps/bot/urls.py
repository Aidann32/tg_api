# from django.urls import path
# from . import views


# urlpatterns = [
#     path('start/', views.start_command, name='start_command'),
# ]

from django.conf import settings
from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('messages', views.MessageViewSet, basename='messages')

urlpatterns = [
    path(f'<str:token>/webhook/', views.telegram_webhook, name='telegram_webhook'),

    path('send_message/', views.send_message, name='send_message'),
    path('', include(router.urls))
]