from django.urls import path

from . import views
from django.contrib.auth import views as auth_views



app_name = "crm"

urlpatterns = [
    path("", views.Statistics.as_view(), name="statistics"),


    path("login/", views.Login.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),


    path("register/seller", views.RegisterSeller.as_view(), name="register_seller"),
    path("register/deliver", views.RegisterDeliver.as_view(), name="register_deliver"),
    path("register/warehouseworker", views.RegisterWarehouseWorker.as_view(), name="register_warehouseworker"),
]