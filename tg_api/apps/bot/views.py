import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import telebot

from .bot import bot
from .models import Message
from .serilaizers import MessageSerializer


class MessageViewSet(ReadOnlyModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user) 


@api_view(['POST', ])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_message(request) -> Response:
        user = request.user
        if not user.chat_id:
            return Response({"message": "User is not linked to any chat"}, status=status.HTTP_404_NOT_FOUND)
        if not request.data.get('message', ''):
            return Response({"message": "Body should contain message value"}, status=status.HTTP_404_NOT_FOUND)
        message = request.data.get('message')
        tg_message = f'{user.username}, я получил от тебя сообщение:\n{message}'
        bot.send_message(user.chat_id, tg_message)
        Message.objects.create(user=user, text=tg_message)
        return Response({'message': 'Message is successfully sended'}, status=status.HTTP_200_OK)

@api_view(['POST',])
@csrf_exempt
def telegram_webhook(request, token: str) -> Response:
    if token == settings.TELEGRAM_TOKEN:
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return Response({'status': 'ok'})
    else:
        return Response({'status': 'invalid token'})


