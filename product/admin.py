from django.contrib import admin
from financial.admin import date_time_translate_jalali
from product.models import Product, AffiliatorProduct


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        "name",
        "view_name",
        "is_active",
        "price",
        "sale_price",
        "affiliator_share",
        "get_create_at_jalali",
        "get_update_at_jalali",
    )
    readonly_fields = ("get_create_at_jalali", "get_update_at_jalali")

    def get_create_at_jalali(self, obj):
        if obj.create_at:
            return date_time_translate_jalali(obj.create_at)

    get_create_at_jalali.short_description = "تاریخ ایجاد"
    get_create_at_jalali.admin_order_field = "create_at"

    def get_update_at_jalali(self, obj):
        if obj.update_at:
            return date_time_translate_jalali(obj.update_at)

    get_update_at_jalali.short_description = "آخرین آپدیت"
    get_update_at_jalali.admin_order_field = "update_at"


admin.site.register(Product, ProductAdmin)
admin.site.register(AffiliatorProduct)
