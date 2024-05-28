from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel Admin'

        return context