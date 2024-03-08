from datetime import datetime, date
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

from .utils import(
                    most_sold_product, 
                    most_buy_customer,
                    debt_sale,
                    cash_sale,
                    expances,
                )
from shop.models import Product, OrderItems
def is_seller(user):
    if user.is_authenticated:
        return user.is_seller
    return False

def is_superuser(user):
    if user.is_authenticated:
        return user.is_superuser
    return False

superuser_required = user_passes_test(is_superuser, login_url=None, redirect_field_name=None)

seller_required = user_passes_test(is_seller, login_url=None, redirect_field_name=None)



@method_decorator(login_required, name='dispatch')
class Statistics(View):
    template_name = "crm/index.html"


    def get_context_data(self, *kwargs):
        product_id = most_sold_product()
        customer = most_buy_customer()
        debt = debt_sale()
        cash = cash_sale()
        expance = expances()
        sale = debt + cash
        if expance is None:
            expance = "Ma'lumot mavjud emas"
        if sale is None:
            sale = "Ma'lumot mavjud emas"
        if cash is None:
            cash = "Ma'lumot mavjud emas"
        if debt is None:
            debt = "Ma'lumot mavjud emas"
        if customer is None:
            cutomer = "Ma'lumot mavjud emas"
        try:
            product = Product.objects.get(id=product_id)
        except:
            product = "Ma'lumot mavjud emas"
        
        context = {
            "most_sold_product": product,
            "most_buy_customer": customer,
            "debt": debt,
            "cash": cash,
            "expances": expance,
            "expance": expance,
            "sale": sale

        }
        return context
    

    def get(self, reqeust):
        context = self.get_context_data()
        return render(reqeust, self.template_name, context)
    

    def post(self, reqeust):
        context = self.get_context_data()
        if "filter_date" in reqeust.POST:
            start_date_str = reqeust.POST.get("start_date")
            end_date_str = reqeust.POST.get("end_date")
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            product_id  = most_sold_product(start_date, end_date)
            most_buy = most_buy_customer(start_date, end_date)
            debt = debt_sale(start_date, end_date)
            cash = cash_sale(start_date, end_date)
            expance = expances(start_date, end_date)
            if cash is None:
                cash = "Ma'lumot mavjud emas"
            if debt is None:
                debt = "Ma'lumot mavjud emas"
            if most_buy is None:
                most_buy = "Ma'lumot mavjud emas"
            try:
                product = Product.objects.get(id=product_id)
            except:
                product = "Ma'lumot mavjud emas"

            context["most_sold_product"] = product
            context["most_buy_customer"] = most_buy
            context["debt"] = debt
            context["cash"] = cash
            context["expances"] = expance
        return render(reqeust, self.template_name, context)
    

class Login(View):
    template_name = "crm/pages/samples/login.html"


    def get_context_data(self, *kwargs):
        context = {}
        return context


    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)


    def post(self, request):
        context = self.get_context_data()
        if "login" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")


            user = authenticate(request=request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("crm:statistics")
            else:
                return render(request, self.template_name, {'error': 'Parol yoki Username Xato, Qaytadan urinib ko\'ring'})
        return render(request,self.template_name, context)
    

@method_decorator(superuser_required, name='dispatch')
class RegisterSeller(View):
    template_name = "crm/pages/samples/register_seller.html"

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})
    

    def post(self, request):
        if "register" in request.POST:
            form = CustomUserCreationForm(request.POST)
            user_type = request.POST.get("type")
            if form.is_valid():
                user = form.save(commit=False)
                if user_type == "warehouseworker":
                    user.is_warehouseworker = True
                else:
                    user.is_seller = True
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                return redirect('crm:statistics')
            else:
                print(form.errors)
        return render(request, self.template_name, {'form': form})


@method_decorator(superuser_required, name='dispatch')
class RegisterWarehouseWorker(View):
    template_name = "crm/pages/samples/register_warehouseworker.html"

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})
    

    def post(self, request):
        if "register" in request.POST:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_warehouseworker = True
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                return redirect('crm:statistics')
            else:
                print(form.errors)
        return render(request, self.template_name, {'form': form})
    

@method_decorator(superuser_required, name='dispatch')
class RegisterDeliver(View):
    template_name = "crm/pages/samples/register_deliver.html"

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})
    

    def post(self, request):
        if "register" in request.POST:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_deliver = True
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                return redirect('crm:statistics')
            else:
                print(form.errors)
        return render(request, self.template_name, {'form': form})