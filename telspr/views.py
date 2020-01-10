from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView)
from telspr import models
# Create your views here.

class PersonListView(ListView):
    context_object_name = 'persons'
    model = models.Person
    template_name = 'telspr/index.html'
