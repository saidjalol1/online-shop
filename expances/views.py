from django.shortcuts import render, redirect

from django.views import View
from . import models

class Expances(View):
    template_name = "expances/expances.html"


    def get_context_data(self,**kwargs):
        context = {
            "expances" : models.Expances.objects.all()
        }
        return context
    

    def get(self, request):
        context = self.get_context_data()
        print(context["expances"])
        return render(request, self.template_name, context)
    

    def post(self, request):
        context = self.get_context_data()

        if "date_filter" in request.POST:
            context["expances"] = models.Expances.objects.filter(date_added=request.POST.get("date"))
            

        if "delete" in request.POST:
            try:
                expances = models.Expances.objects.get(id =request.POST.get("expance"))
                expances.delete()
            except models.Expances.DoesNotExist:
                return redirect("expances:expance_main")
        
        if "update" in request.POST:
            expance = models.Expances.objects.get(id = request.POST.get("expance"))

        if "create" in request.POST:
            expance = models.Expances.objects.create(
                name = request.POST.get("name"),
                amount = request.POST.get("amount"),
                description = request.POST.get("description"),
            )
            expance.save()
        return render(request, self.template_name, context)