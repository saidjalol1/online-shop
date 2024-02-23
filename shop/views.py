from django.shortcuts import render

from django.views.generic import View


class MainPage(View):
    template_name = "shop/index.html"
    
    def get(self,request):
        context =  {}
        return render(request, self.template_name, context)
    

class WishlistPage(View):
    template_name = "shop/wishlist.html"
    
    def get(self,request):
        context =  {}
        return render(request, self.template_name, context)
    

class CartPage(View):
    template_name = "shop/cart.html"
    
    def get(self,request):
        context =  {}
        return render(request, self.template_name, context)
