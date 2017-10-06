from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, EventsSerializer
from .models import Event
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(user_id=1).order_by('id')
    serializer_class = EventsSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser,
    )

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Event.objects.filter(user_id=user_id)

    # def get_serializer_context(self):
    #     user_id = self.kwargs['user_id']
    #     return {'user_id': user_id}

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
