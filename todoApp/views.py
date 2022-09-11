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

class SearchView(ListView):
    model = Thing
    template_name = 'thing_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Thing.objects.filter(name__contains=query)
            result = postresult
        else:
            result = None
        return result