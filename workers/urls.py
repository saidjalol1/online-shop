from django.urls import path

from . import views

app_name = "workers"
urlpatterns = [
    path("", views.Workers.as_view(), name="workers_main")
]