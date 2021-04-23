from django.shortcuts import render

# Create your views here.
from .models import Contact
from ..blog.models import Post, Category # usando para que eu deixe de usar os links no menu de modo FIXO e seja dinâmico
from .forms import ContactForm


def home(request):
    # TODO: {'categorias_menu' em dois lugares , talvez melhor isso para não dar problema em dois lugares qdo atualizar alguma coisa
    #  .. na view home para qdo carregar da primeira vez e na VIEW BLOG para sem carregar a category.html qdo for chamada}
    categorias_menu = Category.objects.order_by('title') # transformando meu menu em dinâmico
    blog_slide_random = Post.objects.order_by('?')[:4]
    return render(request, 'home/home.html', {'categorias_menu':categorias_menu, 'blog_slide_random':blog_slide_random})

def politica_privacidade(request):
    return render(request, 'home/politica_privacidade.html' )

def termos_uso(request):
    return render(request, 'home/termos_uso.html')

def menu():
    categorias_menu = Category.objects.all() #.order_by('title') # transformando meu menu em dinâmico
    # print(categorias_menu)
    # print(categorias_menu.id)


def contact(request):
    if request.method == 'POST':
        # print('0')
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
