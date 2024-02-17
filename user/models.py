from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_AFFILIATOR = "affiliator"
    USER_TYPE_SELLER = "seller"
    USER_TYPES = (
        (USER_TYPE_AFFILIATOR, "Affiliator"),
        (USER_TYPE_SELLER, "Seller"),
    )

    email = models.EmailField(_("email address"), blank=True, unique=True)
    username = models.CharField(_("Username"), max_length=50, blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(
        max_length=64, default=USER_TYPE_AFFILIATOR, choices=USER_TYPES
    )

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = [
        "email",
    ]

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = "user"


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        related_name="profile",
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(_("First name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last name"), max_length=50, blank=True, null=True)
    phone = models.CharField(_("Phone number"), max_length=50, blank=True, null=True)
