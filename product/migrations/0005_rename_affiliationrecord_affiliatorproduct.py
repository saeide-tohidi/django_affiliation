# Generated by Django 3.2.9 on 2021-11-21 17:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0004_auto_20211121_1725"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AffiliationRecord",
            new_name="AffiliatorProduct",
        ),
    ]