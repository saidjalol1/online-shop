from django.urls import path

from . import views

app_name = "shop"

urlpatterns =  [
    path("", views.MainPage.as_view(), name="main"),
    path("wishlist/", views.WishlistPage.as_view(), name="wishlist"),
    path("cart/", views.CartPage.as_view(), name="cart"),
    path("add_to_cart/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("add_to_wishlist/<int:product_id>", views.add_to_wishlist, name="add_to_wishlist"),
    path("remove_from_cart/<int:product_id>", views.remove_from_cart, name="remove_from_cart"),
]
