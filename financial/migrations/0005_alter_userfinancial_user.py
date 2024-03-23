# Generated by Django 4.2.10 on 2024-03-23 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("financial", "0004_userpaymentrequestrecord"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfinancial",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="financial",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
    ]
