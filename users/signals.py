from django.db.models.signals import post_save # kind of trigger to trigger another command when an entry is created in database
from django.contrib.auth.models import User
from django.dispatch import receiver # a listner to receive the signal
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()