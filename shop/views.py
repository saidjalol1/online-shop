import random
import string
from django.shortcuts import render, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib import messages

from django.views.generic import View

from . import models

# Bar code for Orders
from django.shortcuts import render
from django.http import HttpResponse
from barcode import Code128
from barcode.writer import ImageWriter

from .models import Barcode
from .utils import generate_barcode_data, generate_barcode_image 


class MainPage(View):
    template_name = "shop/index.html"
    products_per_page = 4

    def get_context_data(self, **kwargs):
        context = {}
        session_key = self.request.session.session_key

        if not session_key:
            self.request.session.save()
            session_key = self.request.session.session_key
        

        all_products = models.Product.objects.all()
        paginator = Paginator(all_products, self.products_per_page)
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        
        context.update({
            "products": products,
            "categories": models.Category.objects.all(),
        })
        return context

    def get(self,request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

class WishlistPage(View):
    template_name = "shop/wishlist.html"
    products_per_page = 4

    def get_context_data(self, **kwargs):
        context = {}
        session_key = self.request.session.session_key


        all_products = models.WishlistItem.objects.filter(session_key=session_key)

        paginator = Paginator(all_products, self.products_per_page)
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context.update({
            "products": products,
        })
        return context 


    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

    def post(self, request):
        context = self.get_context_data()
        
        if "remove" in request.POST:
            try:
                wishlist = models.WishlistItem.objects.get(session_key = request.session.session_key, product_id= request.POST.get("product"))
                wishlist.delete()
            except ObjectDoesNotExist:
                return redirect("shop:wishlist")
        return render(request, self.template_name, context)


class CartPage(View):
    template_name = "shop/cart.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        session_key = self.request.session.session_key


        all_products = models.CartItems.objects.filter(session_key=session_key)

        context.update({
            "products": all_products,
        })
        return context 


    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

    def post(self, request):
        context = self.get_context_data()
        if "order" in request.POST:
            order = models.Order.objects.create(
                name=request.POST.get("customer_name"),
                phone=request.POST.get("customer_phone"),
                region=request.POST.get("customer_city_region"),
                street=request.POST.get("customer_street"),
                target=request.POST.get("customer_target"),
            )
            barcode_data = generate_barcode_data()  
            barcode = Barcode.objects.create(order=order, barcode_data=barcode_data)

            
            barcode_image_path = generate_barcode_image(barcode_data, order.id) 
            order.barcode_image = barcode_image_path  
            order.save()  
            
            for cart_item in models.CartItems.objects.filter(session_key=request.session.session_key):
                order_item = models.OrderItems.objects.create(
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    session_key=cart_item.session_key,
                    order=order
                )
                cart_item.delete()
                print("Order Itemlar >>>>>>>>>>", order_item)
        
            messages.success(request, 'Buyurtmangiz qabul qilindi')
            

        if "remove" in request.POST:
            try:
                cart_item = models.CartItems.objects.get(session_key = request.session.session_key, product_id= request.POST.get("product"))
                cart_item.delete()
            except ObjectDoesNotExist:
                return redirect("shop:cart")
        return render(request, self.template_name, context)
    

def add_to_cart(request, product_id):
    product = models.Product.objects.get(id=product_id)
    session_key = request.session.session_key
    try:
        cart_item = models.CartItems.objects.get(session_key=session_key, product__id = product.id)
        cart_item.quantity += 1
        cart_item.save()
        print(int(cart_item.overall_price()))
        response_data = {'success': True, 'new_added': False, "overall_sum" : cart_item.overall_price()}
    except models.CartItems.DoesNotExist:
        cart_item = models.CartItems.objects.create(
            product_id = product.id,
            session_key = session_key
        )
        cart_item.quantity += 1
        cart_item.save()
        response_data = {'success': True, 'new_added': True}
    return JsonResponse(response_data)


def add_to_wishlist(request, product_id):
    product = models.Product.objects.get(id=product_id)
    session_key = request.session.session_key
    try:
        wishlist_item = models.WishlistItem.objects.get(session_key=session_key, product__id = product.id)
        wishlist_item.delete()
        print("Deleted")
        response_data = {'success': True, 'removed': True}
    except models.WishlistItem.DoesNotExist:
        wishlist_item = models.WishlistItem.objects.create(
            product = product,
            session_key = session_key
        )
        wishlist_item.save()
        response_data = {'success': True, 'removed': False}
    return JsonResponse(response_data)


def remove_from_cart(request, product_id):
    session_key = request.session.session_key
    try:
        cart_item = models.CartItems.objects.get(session_key=session_key,product_id = product_id)
        cart_item.quantity -= 1
        cart_item.save()
        overall_sum = cart_item.overall_price()
        print(int(cart_item.overall_price()))
        if cart_item.quantity == 0:
            cart_item.delete()
        deleted = False
        if cart_item.quantity == 0:
            deleted =  True
        else:
            pass
        response_data = {'message': 'Product removed from cart successfully.', "deleted": deleted,"removed": True, "overall_sum" : overall_sum}
    except models.CartItems.DoesNotExist:
        pass
        response_data = {'success': True, "removed": False}
    return JsonResponse(response_data)

