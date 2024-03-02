from django.urls import path
from . import views


urlpatterns = [
    path("products/list/", views.ProductListView.as_view(), name="product_list"),
    path("product/<pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]
