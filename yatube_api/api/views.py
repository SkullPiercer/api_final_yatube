from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

from posts.models import Comment, Group, Post
from .permissions import Author
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, Author)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, Author)

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


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()
