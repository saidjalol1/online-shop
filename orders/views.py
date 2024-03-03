from django.shortcuts import render

from django.views import View
from shop import models
# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test


def is_seller(user):
    if user.is_authenticated:
        return user.is_seller
    return False

seller_required = user_passes_test(is_seller, login_url=None, redirect_field_name=None)


# @method_decorator(seller_required, name='dispatch')
class Orders(View):
    template_name = "orders/active_orders.html"

    def get_context_data(self, *kwargs):
        context = {}
        context.update({
            "orders": models.Order.objects.all()
        })
        return context 
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = self.get_context_data()
        
        if "active" in request.POST:
            context["orders"] = models.Order.objects.filter(status="Active")
            context["status"] = "Active"
        
        if "unactive" in request.POST:
            context["orders"] = models.Order.objects.filter(status="Unactive")
            context["status"] = "NoActive"

        return render(request, self.template_name, context)
    

class OrdersDetail(View):
    template_name = "orders/order_detail.html"


    def get_context_data(self, **kwargs):
        context = {}
        item = models.Order.objects.get(id=self.kwargs.get("pk"))
        context.update({
            "item" : item,
        })
        return context
    

    def get(self, request, **kwargs):
        context = self.get_context_data()
        return render(request,self.template_name, context)
    

    def post(self, request, **kwargs):
        context = self.get_context_data()
        if "print" in request.POST:
            print_order(request, context["item"].id)
        return render(request, self.template_name, context)
    

def print_order(request, pk):
    item = models.Order.objects.get(id=pk)
    context = {
        'item': item,
    }
    print("Ishladi")
    return render(request, 'orders/orders_print.html', context)