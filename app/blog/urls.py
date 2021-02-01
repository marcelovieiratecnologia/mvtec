from django.urls import path
from .views import *


urlpatterns = [
    path('', indexblog, name='blog'),
]