from django.urls import path
from .views import *


urlpatterns = [
    # path('', indexblog, name='blog'),
    path('blogs/', blogs, name='blogs'),
    path('blog-detail/<int:id>/<slug:slug>', blog_detail, name='blogdetail'),
    # path('categorias-menu', categoriasMenu, name='categoriasMenu'),
    path('category-python/', category_python, name='categorypython'),
    path('category-django/', category_django, name='categorydjango'),
    path('category-laravel/', category_laravel, name='categorylaravel'),
    path('category-mysql/', category_mysql, name='categorymysql'),
    path('category-vulnerabilidades/', category_vulnerabilidades, name='categoryvulnerabilidades'),
    path('add-comment/<int:id>/', add_comment, name='addcomment'),

]