from django.urls import path
from .views import *


urlpatterns = [
    path('', indexblog, name='blog'),
    path('blogs/', blogs, name='blogs'),
    path('blog-detail/<int:id>/<slug:slug>/', blogDetail, name='blogdetail'),
    # path('categorias-menu', categoriasMenu, name='categoriasMenu'),
    path('category-python/', categoryPython, name='categorypython'),
    path('category-django/', categoryDjango, name='categorydjango'),
    path('category-laravel/', categoryLaravel, name='categorylaravel'),
    path('category-mysql/', categoryMysql, name='categorymysql'),
    path('category-vulnerabilidades/', categoryVulnerabilidades, name='categoryvulnerabilidades'),
    path('add-comment/<int:id>/', addcomment, name='addcomment'),

]