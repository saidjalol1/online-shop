from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("active_orders/", views.Orders.as_view(), name="active_orders"),
    path("<int:pk>/", views.OrdersDetail.as_view(), name="detail"),
    path("print/<int:pk>/", views.print_order, name="print_order"),
    path("debt/", views.OrderDebt.as_view(), name="debt_order")
]