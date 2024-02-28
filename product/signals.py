from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product, AffiliatorProduct
from user.models import UserProfile


@receiver(post_save, sender=Product)
def create_affiliation_record(sender, instance, created, **kwargs):
    if created:
        users = UserProfile.objects.all()
        for u in users:
            affiliation_r = AffiliatorProduct()
            affiliation_r.user = u.user
            affiliation_r.product = instance
            affiliation_r.name = instance.name
            affiliation_r.price = instance.price
            affiliation_r.sale_price = instance.sale_price
            affiliation_r.affiliator_share = instance.affiliator_share
            affiliation_r.save()
