from django.urls import path

from . import views

app_name = "expances"
urlpatterns = [
    path("", views.Expances.as_view(), name="expance_main"),
]