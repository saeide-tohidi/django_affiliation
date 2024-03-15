from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Lead(models.Model):
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lead",
        verbose_name=_("کاربر"),
    )
    affiliator_product = models.ForeignKey(
        "product.AffiliatorProduct",
        on_delete=models.CASCADE,
        related_name="product_lead",
        verbose_name=_("محصول"),
    )
    full_name = models.CharField(_("لید"), max_length=100)
    phoneNo = models.CharField(_("موبایل"), max_length=14, null=True, blank=True)
    email = models.EmailField(_("ایمیل"), null=True, blank=True)
    price = models.IntegerField(_("قیمت"), blank=True, null=True)
    sale_price = models.IntegerField(_("قیمت حراج"), blank=True, null=True)
    affiliator_share = models.IntegerField(_("سهم افلییتور"), blank=True, null=True)

    STATUS_NEW = "N"
    STATUS_FIRST_CONTACT = "F"
    STATUS_REJECT = "R"
    STATUS_BUY = "B"
    STATUS_GUARANTEE = "G"
    STATUS_FINALIZE = "F"

    STATUS_TYPES = (
        (STATUS_NEW, "جدید"),
        (STATUS_FIRST_CONTACT, "تماس"),
        (STATUS_REJECT, "رد"),
        (STATUS_BUY, "پرداخت اولیه"),
        (STATUS_GUARANTEE, "بازگشت وجه به علت گارانتی"),
        (STATUS_FINALIZE, "خرید نهایی"),
    )
    status = models.CharField(
        _("وضعیت"), max_length=5, choices=STATUS_TYPES, default="N"
    )
    create_at = models.DateTimeField(_("تاریخ ایجاد"), auto_now_add=True)
    update_at = models.DateTimeField(_("آخرین آپدیت"), auto_now=True)

    def __str__(self):
        return self.assignee.profile.full_name

    class Meta:
        verbose_name = _("لید")
        verbose_name_plural = _("لیدها")
        ordering = ["-id"]
