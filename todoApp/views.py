from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from todoApp.models import Thing
from django.db.models import Q
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
class ThingsList(ListView):
    model = Thing
    template_name = 'home.html'
    context_object_name = 'thing'


class CreateThing(LoginRequiredMixin,CreateView):
    model = Thing
    template_name = 'create_thing.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        super(CreateThing, self).form_valid(form)
        return redirect('home')


class SearchView(LoginRequiredMixin, ListView):
    model = Thing
    template_name = "thing_search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("search")
        object_list = Thing.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class DeleteThingView(DeleteView):
    model = Thing
    template_name = "delete_thing.html"
    context_object_name = "thing"
    success_url = reverse_lazy('home')


class EditThingView(UpdateView):
    model = Thing
    template_name = "update_thing.html"
    context_object_name = 'thing'
    fields = '__all__'
    success_url = reverse_lazy('home')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("home")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="registration/login.html", context={"login_form": form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="registration/login.html",
        context={'form': form}
    )

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
