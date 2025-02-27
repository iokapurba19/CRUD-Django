from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'  # The template for the dashboard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context
        # You can add more context variables here if needed
        context['message'] = 'Welcome to the Dashboard!'  # Example context
        return context
