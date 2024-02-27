from . import models
def wishlist_count(request):
    session_key = request.session.session_key
    items = [i for i in models.WishlistItem.objects.filter(session_key = session_key)]
    cart_items = [i for i in models.CartItems.objects.filter(session_key = session_key)]
    return {
        "count_wishlist":len(items),
        "items":[i.product_id for i in items],
        "cart_items": len(cart_items)
        }