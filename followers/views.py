from rest_framework import generics, permissions
from .serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    