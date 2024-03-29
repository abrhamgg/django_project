from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client

@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        client = Client.objects.create(user=instance, name=instance.username)
        client.save()