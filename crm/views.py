from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

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


@method_decorator(login_required, name='dispatch')
class Statistics(View):
    template_name = "crm/index.html"


    def get_context_data(self, *kwargs):
        context = {}
        return context
    

    def get(self, reqeust):
        context = self.get_context_data()
        return render(reqeust, self.template_name, context)
    

    def post(self, reqeust):
        context = self.get_context_data()
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
            if user is not None:
                login(request, user)
                return redirect("crm:statistics")
            else:
                return render(request, self.template_name, {'error': 'Parol yoki Username Xato, Qaytadan urinib ko\'ring'})
        return render(request,self.template_name, context)