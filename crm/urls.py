from django.urls import path

from . import views

app_name = "crm"

urlpatterns = [
    path("", views.Statistics.as_view(), name="statistics"),
    path("icons/", views.Icons.as_view(), name="icons"),
]