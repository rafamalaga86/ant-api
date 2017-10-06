from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
        extra_kwargs = {
                'password': {'write_only': True}
        }


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'frequency', 'date')

    def create(self, validated_data):
        import pdb; pdb.set_trace()
        user_id = self.context['user_id']
        validated_data['user_id'] = User.objects.get(pk=user_id)
        event = Event.objects.create(**validated_data)
        return event
