from django.urls import path
from . import views
from .views import *

# from .views import *
urlpatterns = [
    path('', ThingsList.as_view(), name='home'),
    path('create/', CreateThing.as_view(), name='create_thing'),
    path('results/', SearchView.as_view(), name='search'),
]
