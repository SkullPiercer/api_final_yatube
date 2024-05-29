from django.urls import path
from .views import PostViewSet
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'v1/posts', PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
