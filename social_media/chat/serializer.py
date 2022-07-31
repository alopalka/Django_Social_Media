from rest_framework import serializers
from chat.models import Message
from chat.models import ChatRoom

class MessageSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    creation_date = serializers.DateTimeField(format="%d-%b-%Y, %I:%M")

    class Meta:
        model = Message
        fields = [
            'room',
            'user',
            'content',
            'creation_date',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

class CreateChatSerializer(serializers.ModelSerializer):

    user_creating = serializers.CharField(max_length=200)
    user_added = serializers.CharField(max_length=200)

    class Meta:
        model=ChatRoom
        fields=['user_creating','user_added']
    

class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'room',
            'user',
            'content'
        ]
