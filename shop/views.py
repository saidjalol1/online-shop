from django.shortcuts import render

from django.views.generic import View

class MainPage(View):
    template_name = "shop/index.html"
    
    def get(self,request):
        context =  {}
        return render(request, self.template_name, context)
