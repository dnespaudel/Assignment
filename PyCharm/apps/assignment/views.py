from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser

from apps.assignment import serializers
from apps.assignment.usecase import AddMailUseCase


class AddMailView(generics.CreateAPIView):
    """
    Use this endpoint to add mail
    """
    serializer_class = serializers.AddMailSerializer
    parser_classes = (FormParser, MultiPartParser)

    def perform_create(self, serializer):
        return AddMailUseCase(serializer=serializer, request=self.request).execute()


