from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from posts.models import Comment, Follow, Group, Post
from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    GroupSerializer,
    FollowSerializer,
    PostSerializer
)


def get_post(post_id):
    return get_object_or_404(Post, id=post_id)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        post = get_post(self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_post(self.kwargs['post_id'])
        return post.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
