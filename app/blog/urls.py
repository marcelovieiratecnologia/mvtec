from django.urls import path
from .views import *


urlpatterns = [
    path('', indexblog, name='blog'),
    path('blogs', blogs, name='blogs'),
    path('blogdetail/<int:id>/<slug:slug>', blogDetail, name='blogdetail'),
    path('categorypython', categoryPython, name='categorypython'),
    path('categorydjango', categoryDjango, name='categorydjango'),
    path('categorylaravel', categoryLaravel, name='categorylaravel'),
    path('categorymysql', categoryMysql, name='categorymysql'),
    path('categoryvulnerabilidades', categoryVulnerabilidades, name='categoryvulnerabilidades'),
    path('addcomment/<int:id>', addcomment, name='addcomment'),

]