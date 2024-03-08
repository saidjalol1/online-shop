from django.shortcuts import render, redirect
from shop.models import Product, Category, Order
from . import models
from sale.models import SailItems

from django.views import View
# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


def is_superuser(user):
    if user.is_authenticated:
        return user.is_superuser
    return False

superuser_required = user_passes_test(is_superuser, login_url=None, redirect_field_name=None)



@method_decorator(login_required, name='dispatch')
class WareHouse(View):
    template_name ="warehouse/warehouse.html"


    def get_context_data(self, **kwargs):
        context = {
            "products" : Product.objects.all(),
            "category" : Category.objects.all(),
            "essential": models.EssentialProducts.objects.all(),
        }
        return context
    

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

    def post(self, request):
        context = self.get_context_data()


        if "add_essential_product" in request.POST:
            product = models.EssentialProducts.objects.create(
                name = request.POST.get("name")
            )
            print(product)
            product.save()


        if "delete_essential_product" in request.POST:
            try:
                product = models.EssentialProducts.objects.get(id= request.POST.get("product_id"))
                product.delete()
            except models.EssentialProducts.DoesNotExist:
                return redirect("warehouse:warehouse_main")
        

        if "create" in request.POST:
            product = Product.objects.create(
                name = request.POST.get("name"),
                amount = request.POST.get("amount"),
                image = request.FILES.get("product_image"),
                price = request.POST.get("price"),
                description = request.POST.get("description"),
                category = Category.objects.get(id=request.POST.get("category")),
            )


        if "category_add" in request.POST:
            category_name = request.POST.get("category_name")
            Category.objects.create(
                name = category_name,
                slug=category_name
            )

        if "delete_category" in request.POST:
            try:
                category = Category.objects.get(id= request.POST.get("category"))
                category.delete()
            except Category.DoesNotExist:
                return redirect("warehouse:warehouse_main")
            

        if "add" in request.POST:
            product = Product.objects.get(id=request.POST.get("product"))
            user = request.user
            try:
                sale_item = SailItems.objects.get(user=user, product__id = product.id)
                sale_item.quantity += int(request.POST.get("quantity"))
                sale_item.save()
            except SailItems.DoesNotExist:
                sale_item = SailItems.objects.create(
                    product_id = product.id,
                    user = user
                )
                sale_item.quantity += int(request.POST.get("quantity"))
                sale_item.save()
        return render(request, self.template_name, context)

