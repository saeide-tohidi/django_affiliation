from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("crm/", include("dashboard.urls")),
    path("crm/", include("user.urls")),
    path("crm/", include("financial.urls")),
    path("crm/", include("product.urls")),
    path("crm/", include("crm.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
