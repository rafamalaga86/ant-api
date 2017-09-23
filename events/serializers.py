from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'frequency', 'date')
