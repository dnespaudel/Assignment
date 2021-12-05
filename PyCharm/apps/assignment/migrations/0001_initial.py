# Generated by Django 3.2.9 on 2021-12-04 16:32

import apps.assignment.utils
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=apps.assignment.utils.mail_image_to)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
            },
        ),
    ]