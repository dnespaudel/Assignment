from django.urls import path
from apps.assignment import views

urlpatterns = [
    path('add', views.AddMailView.as_view())
]
