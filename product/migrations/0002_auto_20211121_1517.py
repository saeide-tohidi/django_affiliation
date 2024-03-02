# Generated by Django 3.2.9 on 2021-11-21 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="creat_at",
            new_name="create_at",
        ),
        migrations.CreateModel(
            name="AffiliationRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.CharField(max_length=100, verbose_name="اسلاگ")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="فعال/غیرفعال"),
                ),
                (
                    "product_name",
                    models.CharField(max_length=100, verbose_name="عنوان"),
                ),
                ("product_price", models.IntegerField(verbose_name="قیمت")),
                (
                    "product_sale_price",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="قیمت حراج"
                    ),
                ),
                (
                    "affiliator_share",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="سهم افلیتور"
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="آخرین آپدیت"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="affiliation_product_record",
                        to="product.product",
                        verbose_name="محصول",
                    ),
                ),
                (
                    "user_financial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="affiliation_record",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "محصول افلییتور",
                "verbose_name_plural": "محصولات افلییتور",
                "ordering": ["-id"],
            },
        ),
    ]