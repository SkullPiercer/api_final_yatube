from .views import PostViewSet, CommentViewSet
from django.urls import include, path
from rest_framework import routers


v1_router = routers.DefaultRouter()
v1_router.register(r'v1/posts', PostViewSet)
v1_router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet)
urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
