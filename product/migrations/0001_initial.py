# Generated by Django 3.2.9 on 2021-11-21 06:20

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100, verbose_name="عنوان")),
                (
                    "description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="توضیحات"
                    ),
                ),
                ("view_name", models.CharField(max_length=100, verbose_name="ویو")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="فعال/غیرفعال"),
                ),
                ("price", models.IntegerField(verbose_name="قیمت")),
                (
                    "sale_price",
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
                    "creat_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="آخرین آپدیت"),
                ),
            ],
            options={
                "verbose_name": "محصول",
                "verbose_name_plural": "محصولات",
                "ordering": ["-id"],
            },
        ),
    ]