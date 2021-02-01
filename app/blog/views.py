from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexblog(request):
    mensagem = 'OI'
    return render(request, "blog/homeblog.html",{'mensagem':mensagem})