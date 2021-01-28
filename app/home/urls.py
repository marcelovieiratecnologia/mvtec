from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
]
