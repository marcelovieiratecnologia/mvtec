from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from .models import Contact
from .forms import ContactForm


def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == 'POST':
        print('0')
        form = ContactForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            data = Contact()
            data.nome = form.cleaned_data['nome']
            data.email = form.cleaned_data['email']
            data.assunto = form.cleaned_data['assunto']
            data.mensagem = form.cleaned_data['mensagem']
            print('3')
            data.save()
            print('4')
            return HttpResponseRedirect('blog/contact.html')
    form = Contact
    context = {'form':form}
    return render(request, 'blog/contact.html', context)