from django.urls import path
from . import views
from .views import *

# from .views import *
urlpatterns = [
    path('', ThingsList.as_view(), name='home'),
    path('create/', CreateThing.as_view(), name='create_thing'),
    path('results/', SearchView.as_view(), name='search'),
    path('delete/<int:pk>', DeleteThingView.as_view(), name='delete_thing'),
    path('edit/<int:pk>', EditThingView.as_view(), name='edit_thing'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
