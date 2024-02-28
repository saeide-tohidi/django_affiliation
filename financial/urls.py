from django.urls import path
from . import views


urlpatterns = [
    path("financial/info/", views.UserFinancialInfo.as_view(), name="financial_info"),
    path(
        "financial/request_payment/",
        views.UserPaymentRequestView.as_view(),
        name="request_payment",
    ),
]
