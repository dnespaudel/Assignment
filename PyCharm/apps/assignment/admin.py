from django.contrib import admin
from apps.assignment.models import Mail


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'email',
    )
