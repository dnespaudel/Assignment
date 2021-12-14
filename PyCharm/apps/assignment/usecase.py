from apps.assignment.email import SendEmail
from apps.assignment.models import Mail

import os


class AddMailUseCase:
    def __init__(self, serializer, request):
        self.serializer = serializer
        self.data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        self._mail = Mail(**self.data)
        self._mail.save()

        SendEmail(
            context={
                "fullname": self.data['full_name'],
                'image': self._mail.image,
                'host': 'http://127.0.0.1:8000'
            }
        ).send(to=[self.data['email']])
