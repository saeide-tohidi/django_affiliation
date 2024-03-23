from django.contrib import admin
from financial.models import FinancialRecord, UserFinancial, UserPaymentRequestRecord
from jalali_date import datetime2jalali, date2jalali


def date_translate_jalali(date):
    jd = date2jalali(date).strftime("%y-%m-%d")
    persian_months = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]
    tmp = str(jd).split("-")
    month = persian_months[int(tmp[1]) - 1]
    fa_date = tmp[2] + " " + month + " " + tmp[0]
    return fa_date


def date_time_translate_jalali(date):
    jd = datetime2jalali(date).strftime("%y-%m-%d، ساعت %H:%M")
    persian_months = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]
    day = str(jd).split("،")
    tmp = str(day[0]).split("-")
    month = persian_months[int(tmp[1]) - 1]
    fa_date_time = tmp[2] + " " + month + " " + tmp[0] + "،" + str(day[1])
    return fa_date_time


class FinancialRecordListInline(admin.TabularInline):
    model = FinancialRecord
    fields = ("amount", "type", "get_date_jalali")
    readonly_fields = ["amount", "type", "get_date_jalali"]
    show_change_link = True
    max_num = 5
    extra = 0
    can_delete = False

    def get_date_jalali(self, obj):
        if obj.created_at:
            return date_time_translate_jalali(obj.created_at)

    get_date_jalali.short_description = "تاریخ"
    get_date_jalali.admin_order_field = "created_at"

    def has_add_permission(self, request, obj):
        return False


class FinancialRecordAddInline(admin.TabularInline):
    model = FinancialRecord
    fields = ("amount", "type")
    readonly_fields = ["created_at"]
    show_change_link = True
    max_num = 1
    extra = 1
    can_delete = False

    verbose_name = "اضافه کردن سوابق به کیف پول کاربر"
    verbose_name_plural = "اضافه کردن سوابق به کیف پول کاربر"

    def get_queryset(self, request):
        """Alter the queryset to return no existing entries"""
        # get the existing query set, then empty it.
        qs = super(FinancialRecordAddInline, self).get_queryset(request)
        return qs.none()


class UserFinancialAdmin(admin.ModelAdmin):
    model = UserFinancial
    list_display = ("get_full_name", "credit")
    readonly_fields = (
        "user",
        "get_full_name",
    )
    fields = (
        "user",
        "get_full_name",
        "credit",
    )
    inlines = [FinancialRecordListInline, FinancialRecordAddInline]

    def get_full_name(self, obj):
        return obj.user.profile.full_name

    get_full_name.short_description = "کاربر"


class UserPaymentRequestRecordAdmin(admin.ModelAdmin):
    model = UserPaymentRequestRecord
    list_display = (
        "id",
        "get_full_name",
        "amount",
        "get_request_date_jalali",
        "paid",
        "get_paid_date_jalali",
        "get_update_at_jalali",
        "description",
    )
    fields = (
        "user",
        "get_full_name",
        "amount",
        "get_request_date_jalali",
        "paid",
        "paid_date",
        "get_paid_date_jalali",
        "description",
        "get_update_at_jalali",
    )
    readonly_fields = (
        "user",
        "get_full_name",
        "amount",
        "get_request_date_jalali",
        "get_update_at_jalali",
        "get_paid_date_jalali",
    )
    search_fields = (
        "user__profile__first_name",
        "user__profile__last_name",
        "user__phoneNo",
    )
    list_filter = ("request_date", "paid", "paid_date")

    def get_full_name(self, obj):
        return obj.user.profile.full_name

    get_full_name.short_description = "کاربر"

    def get_request_date_jalali(self, obj):
        return date_time_translate_jalali(obj.request_date)

    get_request_date_jalali.short_description = "تاریخ درخواست"
    get_request_date_jalali.admin_order_field = "request_date"

    def get_update_at_jalali(self, obj):
        return date_time_translate_jalali(obj.update_at)

    get_update_at_jalali.short_description = "تاریخ آپدیت"
    get_update_at_jalali.admin_order_field = "update_at"

    def get_paid_date_jalali(self, obj):
        if obj.paid_date:
            return date_time_translate_jalali(obj.paid_date)

    get_paid_date_jalali.short_description = "تاریخ پرداخت"
    get_paid_date_jalali.admin_order_field = "paid_date"


admin.site.register(UserFinancial, UserFinancialAdmin)
admin.site.register(UserPaymentRequestRecord, UserPaymentRequestRecordAdmin)
