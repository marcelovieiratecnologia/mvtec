from django.urls import path
from .views import category, blogs, blog_detail, add_comment #, category_python, category_django, category_laravel, category_mysql, category_vulnerabilidades

app_name = "appblog"

urlpatterns = [
    # path('', indexblog, name='blog'),
    path('blogs/', blogs, name='blogs'),
    path('blog-detail/<int:id>/<slug:slug>', blog_detail, name='blogdetail'),
    path('category/<int:id>', category, name='category'),
    path('add-comment/<int:id>/', add_comment, name='addcomment'),

    # Views desativadas
    # path('category-python/', category_python, name='categorypython'),
    # path('category-django/', category_django, name='categorydjango'),
    # path('category-laravel/', category_laravel, name='categorylaravel'),
    # path('category-mysql/', category_mysql, name='categorymysql'),
    # path('category-vulnerabilidades/', category_vulnerabilidades, name='categoryvulnerabilidades'),

]