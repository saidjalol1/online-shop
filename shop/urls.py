from django.urls import path

from . import views

app_name = "shop"

urlpatterns =  [
    path("", views.MainPage.as_view(), name="main"),
    path("wishlist/", views.WishlistPage.as_view(), name="wishlist"),
    path("cart/", views.CartPage.as_view(), name="cart"),
]