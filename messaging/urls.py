from django.urls import path
from .views import whatsapp_webhook

# urlpatterns = [
#     path("webhook/", whatsapp_webhook, name="whatsapp_webhook"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("messaging/webhook/", views.whatsapp_webhook, name="whatsapp_webhook"),
]
