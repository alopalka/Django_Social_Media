from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from chat.models import Room
from chat.models import Message

@login_required
def list_rooms(request,template="chat/chat_page.html"):
    
    return render(request, template)