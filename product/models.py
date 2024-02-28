from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from product.utils import create_shortened_url


class Product(models.Model):
    name = models.CharField(_("عنوان"), max_length=100)
    description = RichTextUploadingField(_("توضیحات"))
    view_name = models.CharField(_("ویو"), max_length=100)
    is_active = models.BooleanField(_("فعال/غیرفعال"), default=True)
    price = models.IntegerField(_("قیمت"))
    sale_price = models.IntegerField(_("قیمت حراج"), blank=True, null=True)
    affiliator_share = models.IntegerField(_("سهم افلیتور"), blank=True, null=True)
    create_at = models.DateTimeField(_("تاریخ ایجاد"), auto_now_add=True)
    update_at = models.DateTimeField(_("آخرین آپدیت"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("محصول")
        verbose_name_plural = _("محصولات")
        ordering = ["-id"]


class AffiliatorProduct(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("کاربر"),
        on_delete=models.CASCADE,
        related_name="affiliation_record",
    )
    product = models.ForeignKey(
        "product.Product",
        verbose_name=_("محصول"),
        on_delete=models.CASCADE,
        related_name="affiliation_product_record",
    )
    slug = models.CharField(_("اسلاگ"), max_length=100)
    is_active = models.BooleanField(_("فعال/غیرفعال"), default=True)
    name = models.CharField(_("عنوان"), max_length=100)
    price = models.IntegerField(_("قیمت"))
    sale_price = models.IntegerField(_("قیمت حراج"), blank=True, null=True)
    affiliator_share = models.IntegerField(_("سهم افلیتور"), blank=True, null=True)
    create_at = models.DateTimeField(_("تاریخ ایجاد"), auto_now_add=True)
    update_at = models.DateTimeField(_("آخرین آپدیت"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("محصول افلییتور")
        verbose_name_plural = _("محصولات افلییتور")
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_shortened_url(AffiliatorProduct)
        super().save(*args, **kwargs)
