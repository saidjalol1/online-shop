from django.urls import path

from . import views

app_name = "warehouse"

urlpatterns = [
    path("", views.WareHouse.as_view(), name="warehouse_main")
]