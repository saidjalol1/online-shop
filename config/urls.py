from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("shop.urls", namespace="shop")),
    path("crm/", include("crm.urls", namespace="crm")),
    path("crm/orders/", include("orders.urls", namespace="orders")),
    path("expances/", include("expances.urls", namespace="expances")),
    path("workers/", include("workers.urls", namespace="workers")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)