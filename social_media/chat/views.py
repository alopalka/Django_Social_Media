from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from chat.models import ChatRoom
from chat.models import Message
from chat.serializer import ChatSerializer
from chat.serializer import CreateChatSerializer
from chat.serializer import MessageSerializer
from chat.serializer import CreateMessageSerializer
from user.models import SocialAccount

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import random
from itertools import chain


@login_required
def list_rooms(request, template="chat/chat_page.html"):

    rooms1 = ChatRoom.objects.filter(user1=request.user)
    rooms2 = ChatRoom.objects.filter(user2=request.user)

    rooms = list(chain(rooms1, rooms2))

    rooms_users = []

    rooms_users.append(request.user)

    for room in rooms:
        rooms_users.append(room.user1)
        rooms_users.append(room.user2)

    users = SocialAccount.objects.exclude(username__in=rooms_users)

    context = {
        "users": users,
        "text_author": request.user.id,
    }

    return render(request, template, context)


@api_view(['GET'])
def get_user_rooms(request):

    rooms1 = ChatRoom.objects.filter(user1=request.user)
    rooms2 = ChatRoom.objects.filter(user2=request.user)

    rooms = list(chain(rooms1, rooms2))

    serializer = ChatSerializer(rooms, many=True)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_chatroom(request):
    serializer = CreateChatSerializer(data=request.data)

    if serializer.is_valid():

        user_creating = SocialAccount.objects.get(
            username=serializer.data['user_creating'])
        user_added = SocialAccount.objects.get(
            username=serializer.data['user_added'])

        exact_same_chat_rooms1 = ChatRoom.objects.filter(
            user1=user_creating, user2=user_added)
        exact_same_chat_rooms2 = ChatRoom.objects.filter(
            user2=user_creating, user1=user_added)

        if exact_same_chat_rooms1.count() > 0 or exact_same_chat_rooms2.count() > 0:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        random_int = random.randint(1000, 1000000)
        room_name = f"room{random_int}"

        chatroom = ChatRoom(
            user1=user_creating, user2=user_added,
            name=room_name, slug=room_name)

        chatroom.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_chat_history(request, slug):
    chat = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(room=chat)

    if messages.count() == 0:
        messages = Message(room=chat, user=chat.user1,
                           content="Send first message to start chatting")

        serializer = MessageSerializer(messages, many=False)
    else:
        serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_message(request):
    serializer = CreateMessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
