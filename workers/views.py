from django.shortcuts import render, redirect

from django.views import View
from . import models

class Workers(View):
    template_name = "workers/workers.html"

    def get_context_data(self, **kwargs):
        context = {
            "workers": models.Workers.objects.all()
        }
        return context
    

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

    def post(self, request):
        context = self.get_context_data()

        if "postion_filter" in request.POST:
            context["workers"] = models.Workers.objects.filter(position=request.POST.get("postion"))
            

        if "delete" in request.POST:
            try:
                workers = models.Workers.objects.get(id =request.POST.get("worker"))
                workers.delete()
            except models.Workers.DoesNotExist:
                return redirect("workers:workers_main")
        

        if "update" in request.POST:
            worker = models.Workers.objects.get(id = request.POST.get("worker"))

        if "create" in request.POST:
            worker = models.Workers.objects.creat(
                name = request.POST.get("name"),
                surname = request.POST.get("surname"),
                position = request.POST.get("position"),
                salary = request.POST.get("salary"),
                phone = request.POST.get("phone"),
            )
            worker.save()
        return render(request, self.template_name, context)