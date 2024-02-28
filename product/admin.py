from django.contrib import admin
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
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(AffiliatorProduct)
