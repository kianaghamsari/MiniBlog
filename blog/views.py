from django.core.cache import cache
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        cache_key = "api:posts:list"
        data = cache.get(cache_key)
        if not data:
            queryset = self.get_queryset()
            data = PostSerializer(queryset, many=True).data
            cache.set(cache_key, data, 300)
        return Response(data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        cache.delete('api:posts:list')

    def perform_update(self, serializer):
        serializer.save()
        cache.delete('api:posts:list')

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete('api:posts:list')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)