from django.urls import path

from . import views

app_name = "crm"

urlpatterns = [
    path("", views.Statistics.as_view(), name="statistics"),
    path("login/", views.Login.as_view(), name="login"),
]