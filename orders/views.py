from django.shortcuts import render

from django.views import View
from shop import models
from crm.models import CustomUser
from shop.models import Barcode, Notification
# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test


# Generate PDF
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def print_pdf(request, pk):
    item = models.Order.objects.get(id=pk)
    
    context = {
        'item': item,
    }

    # Render HTML template to string
    html_string = render_to_string('orders/orders_print.html', context)

    # Generate PDF from HTML string
    pdf = HTML(string=html_string).write_pdf()

    # Prepare response with PDF as attachment
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{pk}.pdf'
    print( response )
    return response

def is_superuser(user):
    if user.is_authenticated:
        return user.is_seller
    return False

def is_seller(user):
    if user.is_authenticated:
        return user.is_seller or is_superuser
    return False

superuser_required = user_passes_test(is_superuser, login_url=None, redirect_field_name=None)
seller_required = user_passes_test(is_seller, login_url=None, redirect_field_name=None)


@method_decorator(login_required, name='dispatch')
class Orders(View):
    template_name = "orders/active_orders.html"

    def get_context_data(self, *kwargs):
        context = {}
        orders = models.Order.objects.all()
        for i in orders:
            try:
                notify = Notification.objects.get(order_id=i.id)
                notify.delete()
            except Exception:
                pass
        context.update({
            "orders":orders,
            "delivers": CustomUser.objects.filter(is_deliver=True)
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
        
        if "deliver_submit" in request.POST:
            order = models.Order.objects.get(id=request.POST.get("order"))
            print(order)
            deliver = CustomUser.objects.get(id=request.POST.get("deliver"))

            for i in order.order_items.all():
                product = i.product
                product.sold_amount += i.quantity
                product_amount = int(product.amount)
                product.amount = product_amount - i.quantity
                product.save()

            order.deliver = deliver
            order.status = "Unactive"
            order.save()
        
        if "cash" in request.POST:
            order = models.Order.objects.get(id=request.POST.get("order"))
            order.payment_type = "Naqd"
            order.status = "Unactive"
            order.save()

        if "plastik" in request.POST:
            order = models.Order.objects.get(id=request.POST.get("order"))
            order.payment_type = "Plastik"
            order.status = "Unactive"
            order.save()

        
        return render(request, self.template_name, context)
    

class OrdersDetail(View):
    template_name = "orders/order_detail.html"


    def get_context_data(self, **kwargs):
        context = {}
        item = models.Order.objects.get(id=self.kwargs.get("pk"))

        try:
            notify = Notification.objects.get(order_id=item.id)
            notify.delete()
        except Exception:
            pass

        context.update({
            "item" : item,
            })
        return context
    
    def get(self, request, **kwargs):
        context = self.get_context_data()
        return render(request,self.template_name, context)
    
    def post(self, request, **kwargs):
        context = self.get_context_data()
        if "pdf" in request.POST:
            print_pdf(request, self.kwargs.get("pk"))
        return render(request, self.template_name, context)
    

class OrderDebt(View):
    template_name = "orders/debt_orders.html"

    def get_context_data(self, **kwargs):
        context = {
            "orders" : models.Order.objects.filter(payment_type="Nasiya")
        }
        return context 


    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = self.get_context_data()
        if "mark_deadline" in request.POST:
            order = models.Order.objects.get(id=request.POST.get("order"))
            order.payment_deadline = request.POST.get("deadline")
            order.save()

        return render(request, self.template_name, context)
    

def print_order(request, pk):
    item = models.Order.objects.get(id=pk)
    context = {
        'item': item,
    }
    return render(request, 'orders/orders_print.html', context)