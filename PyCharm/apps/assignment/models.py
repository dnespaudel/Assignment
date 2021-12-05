import uuid

from django.db import models
from apps.assignment.utils import mail_image_to


class BaseModel(models.Model):
    """
    Base Model that will used in this project
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Mail(BaseModel):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=mail_image_to)
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Mail'
        verbose_name_plural = 'Mails'
