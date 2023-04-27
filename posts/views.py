from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


# class PostListView(APIView):
#     serializer_class = PostSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(
#             posts, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, 
#                         status=status.HTTP_400_BAD_REQUEST)

class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()


# class PostDetail(APIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#             self.check_object_permissions(self.request, post)
#             return post
#         except Post.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(
#             post, context={'request': request}
#         )
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(
#             post, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, 
#                         status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()