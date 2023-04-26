from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializer import CommentDetailSerializer, CommentSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

