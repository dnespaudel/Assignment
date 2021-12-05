from rest_framework import serializers
from .models import Mail


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'


class AddMailSerializer(MailSerializer):
    class Meta(MailSerializer.Meta):
        fields = (
            'full_name',
            'image',
            'email',
        )
