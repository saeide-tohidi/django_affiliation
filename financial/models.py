from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class UserFinancial(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        verbose_name=_("کاربر"),
        on_delete=models.CASCADE,
        related_name="financial",
    )
    sheba = models.CharField(_("شماره شبا"), max_length=40, null=True, blank=True)
    card_num = models.CharField(_("شماره کارت"), max_length=30, null=True, blank=True)
    credit = models.IntegerField(_("اعتبار"), default=0)

    def __str__(self):
        return self.user.profile.full_name

    class Meta:
        verbose_name = _("اطلاعات مالی")
        verbose_name_plural = _("اطلاعات مالی")


class FinancialRecord(models.Model):
    user_financial = models.ForeignKey(
        "financial.UserFinancial",
        verbose_name=_("کاربر"),
        on_delete=models.CASCADE,
        related_name="financial_record",
    )
    amount = models.IntegerField(_("مبلغ"), default=0)
    TYPE_DECREASE = "D"
    TYPE_INCREASE = "I"
    ACTION_TYPES = (
        (TYPE_DECREASE, "کسر اعتبار"),
        (TYPE_INCREASE, "افزایش اعتبار"),
    )
    type = models.CharField(_("نوع عملیات"), max_length=50, choices=ACTION_TYPES)
    created_at = models.DateTimeField(_("تاریخ"), auto_now_add=True)

    def __str__(self):
        return self.user_financial.user.profile.full_name

    def save(self, *args, **kwargs):
        if self.type == "D":
            self.user_financial.credit = self.user_financial.credit - self.amount
        else:
            self.user_financial.credit = self.user_financial.credit + self.amount
        self.user_financial.save()
        super(FinancialRecord, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("سوابق مالی")
        verbose_name_plural = _("سوابق مالی")


class UserPaymentRequestRecord(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="payment_request",
        verbose_name=_("کاربر"),
    )
    amount = models.IntegerField(_("مبلغ"), blank=True, null=True)
    paid = models.BooleanField(_("پرداخت شده"), default=False)
    description = models.TextField(_("توضیحات"), blank=True, null=True)
    request_date = models.DateTimeField(_("تاریخ درخواست"), auto_now_add=True)
    paid_date = models.DateTimeField(_("تاریخ پرداخت"), null=True, blank=True)
    update_at = models.DateTimeField(_("تاریخ آخرین آپدیت"), auto_now=True)

    def __str__(self):
        return self.user.profile.full_name + " " + ("پرداخت شده" if self.paid else "")

    class Meta:
        verbose_name = _("درخواست تسویه حساب")
        verbose_name_plural = _("درخواست تسویه حساب")
        ordering = ["-id"]
