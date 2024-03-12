from django.urls import path
from . import views


urlpatterns = [
    path("sidebar", views.Sidebar.as_view(), name="sidebar"),
    path("header", views.Header.as_view(), name="header"),
    path("", views.Dashboard.as_view(), name="crm_dashboard"),
]
