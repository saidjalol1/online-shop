from django.shortcuts import render, redirect

from django.views import View
from . import models
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
class Workers(View):
    template_name = "workers/workers.html"

    def get_context_data(self, **kwargs):
        context = {
            "workers": models.Workers.objects.all(),
            "positions": models.Positions.objects.all()
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
            worker = models.Workers.objects.create(
                name = request.POST.get("name"),
                surname = request.POST.get("surname"),
                position = request.POST.get("position"),
                salary = request.POST.get("salary"),
                phone = request.POST.get("phone"),
            )
            worker.save()
        
        if "debt_add" in request.POST:
            try:
                workers = models.Workers.objects.get(id =request.POST.get("worker"))
                workers.debt = request.POST.get("debt")
                workers.save()
            except models.Workers.DoesNotExist:
                return redirect("workers:workers_main")
        if "position_add" in request.POST:
            position = models.Positions.objects.create(
                name=request.POST.get("name")
            )
            position.save()
        return render(request, self.template_name, context)