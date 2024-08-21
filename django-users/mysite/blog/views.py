# blog/views.py
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/protected.html'
