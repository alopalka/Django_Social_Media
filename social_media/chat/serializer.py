from rest_framework import serializers
from chat.models import Message

class MessageSerializer(serializers.ModelSerializer):

    user=serializers.SerializerMethodField()
    creation_date=serializers.DateTimeField(format="%d-%b-%Y, %I:%M")

    class Meta:
        model = Message
        fields = [
            'room',
            'user',
            'content',
            'creation_date',
        ]

    def get_user(self,obj):
        return str(obj.user.username)