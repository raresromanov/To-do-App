from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from todoApp.models import Thing


# Create your views here.
class ThingsList(ListView):
    model = Thing
    template_name = 'home.html'
    context_object_name = 'thing'

class CreateThing(CreateView):
    model = Thing
    template_name = 'create_thing.html'
    fields = '__all__'
    success_url = reverse_lazy('home')