from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic

class LoggedInView(generic.TemplateView):
    template_name = 'index.html'
