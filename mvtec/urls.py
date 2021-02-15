"""mvtec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView  # No Momento Fora de USO , estou usando o Include e não o TemplateView


urlpatterns = [
    path('admin', admin.site.urls),
    # path('', include('app.home.urls')), # aponta para home tb .. como pode ver essa e a debaixo aponta para mesmo URLS
    # path('home/', include('app.home.urls')),   # path('', TemplateView.as_view(template_name='home.html')),
    path('blog/', include('app.blog.urls')),   # path('', TemplateView.as_view(template_name='home.html')),
    path('calculaHorasDia/', include('app.calculaHorasDia.urls')), # path('calculaHorasDia/', TemplateView.as_view(template_name='calculaHorasDia/teste.html')),
    # path('blog/', include('app.blog.urls')),
    path('', include('app.blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')), # conforme solicitado no manual o CKEDITOR (GitHub CkEditor Django) adicionei essas linha

]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) **** ESTOU USANDO DA FORMA QUE ESTA ABAIXO

if settings.DEBUG:
    #para funcionar os arquivos estaticos em DEBUG (Images, css, javascript, etc .)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
