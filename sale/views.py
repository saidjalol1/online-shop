from django.shortcuts import render
from . import models
from shop.models import Order, OrderItems
from django.views import View
# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from shop.models import Barcode
from shop.utils import generate_barcode_data, generate_barcode_image 




@method_decorator(login_required, name='dispatch')
class SaleMain(View):
    template_name = "sale/sale.html"


    def get_context_data(self, **kwargs):
        context = {
            "products" : models.SailItems.objects.all()
        }
        return context
    

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

    def post(self, request):
        context = self.get_context_data()
        if "order" in request.POST:
            order = Order.objects.create(
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
            
            for i in models.SailItems.objects.filter(user=request.user):
                sale_item = OrderItems.objects.create(
                    product=i.product,
                    quantity=i.quantity,
                    order=order
                )
                
                i.delete()
        return render(request, self.template_name, context)
    