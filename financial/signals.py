from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from financial.models import UserFinancial
from user.models import UserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_financial(sender, instance, created, **kwargs):
    if created or not hasattr(instance, "financial"):
        financial = UserFinancial()
        financial.user = instance
        financial.save()
