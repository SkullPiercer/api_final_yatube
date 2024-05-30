from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class CreateAuthorMixin:
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)