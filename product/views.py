from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from product.models import Product, AffiliatorProduct


class ProductListView(LoginRequiredMixin, ListView):
    model = AffiliatorProduct
    queryset = AffiliatorProduct.objects.filter(is_active=True)
    template_name = "product/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.all()
        affiliator_record = []
        for product in products:
            if AffiliatorProduct.objects.filter(
                product=product, user=self.request.user
            ).exists():
                affiliation_r = AffiliatorProduct.objects.get(
                    product=product, user=self.request.user
                )
            else:
                affiliation_r = AffiliatorProduct()
                affiliation_r.user = self.request.user
                affiliation_r.product = product
                affiliation_r.name = product.name
                affiliation_r.price = product.price
                affiliation_r.sale_price = product.sale_price
                affiliation_r.affiliator_share = product.affiliator_share
                affiliation_r.save()
            affiliator_record.append(affiliation_r)
        context["products"] = affiliator_record
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"
