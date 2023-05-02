from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        client = Client.objects.create(user=instance, name=instance.username)
        client.save()

class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField('Work')

class Work(models.Model):
    LINK_CHOICES = [
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    ]
    link = models.URLField()
    work_type = models.CharField(max_length=15, choices=LINK_CHOICES)