from django.urls import path
from chat import views

app_name="chat"

urlpatterns=[
    path('',views.list_rooms,name="rooms"),
    path('chat-history/<slug:slug>',views.get_chat_history,name="chat-history"),
    path('message-create/',views.create_message,name="create-message"),
]