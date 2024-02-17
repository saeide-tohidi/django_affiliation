from django.utils.text import slugify
from user.models import (
    User,
    UserProfile,
)
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, "profile"):
        UserProfile.objects.create(user=instance)
