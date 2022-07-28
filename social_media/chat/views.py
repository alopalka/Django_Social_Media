from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from chat.models import ChatRoom
from chat.models import Message
from chat.serializer import MessageSerializer
from chat.serializer import CreateMessageSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from itertools import chain


@login_required
def list_rooms(request, template="chat/chat_page.html"):

    rooms1 = ChatRoom.objects.filter(user1=request.user)
    rooms2 = ChatRoom.objects.filter(user2=request.user)

    rooms = list(chain(rooms1, rooms2))

    context = {
        "rooms": rooms,
        "text_author": request.user.id,
    }

    return render(request, template, context)


@api_view(['GET'])
def get_chat_history(request, slug):
    chat = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(room=chat)
    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_message(request):
    serializer = CreateMessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
