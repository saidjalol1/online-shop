from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


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
    
    
class Icons(TemplateView):
    template_name = "crm/pages/icons/mdi.html"
