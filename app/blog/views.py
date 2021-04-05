from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# My Views Creates
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.
def indexblog(request):
    categorys = Category.objects.all()
    blog_slide_random = Post.objects.order_by('?')[:4]  # Aqui estou montando o SLIDE de forma randomica  e com apenas 4
    blog_latest = Post.objects.order_by('id')[:8]  # Aqui estou montanto o meu conteúdo para a página e apenas 8 últimos
    conteudo = {
                'blog_slide_random': blog_slide_random,
                'blog_latest': blog_latest,
                'categorys': categorys,
                }
    return render(request, "blog/bloghome.html", conteudo)


def category_menu(request):
    categorias_menu = Category.objects.order_by('title')
    return render(request, 'blog/categorys.html', {'category_menu': category_menu})


def category(request, id):
    categorias_menu = Category.objects.order_by('title')  # transformando meu menu em dinâmico
    category = Post.objects.filter(category_id=id)
    categorys_tag = Category.objects.all()
    blog_latest = Post.objects.order_by('id')[:6]  # Aqui estou montanto o meu conteúdo para a página e apenas 6 últimos
    # TODO: tentando monstrar os comentários
    # total = Comment.objects.filter(post_id=id, status='Lido').count()
    context = {
                'categorias_menu':categorias_menu,
                'category': category,
                'blog_latest': blog_latest,
                'categorys_tag': categorys_tag,
                # 'totalcomments': totalcomments,
               }
    return render(request, 'blog/categorys.html', context)


def blogs(request):
    categorias_menu = Category.objects.order_by('title')  # transformando meu menu em dinâmico
    #category = Category.objects.all().order_by('title')
    categorys_tag = Category.objects.all()
    blogs = Post.objects.all()
    blog_latest = Post.objects.order_by('id')[:4]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    # comments = Comment.objects.filter(post_id=id, status='Lido')
    # for c in comments:
    #     print('Comentários ::::::::::::::::::', c['comment'])
    # totalcomments = Comment.objects.filter(post_id=id, status='Lido').count()
    # outro jeito de contar os comentários
    # totalcomments = 0
    # for i in comments:
    #     totalcomments += 1

    paginator = Paginator(blogs, 3)  # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content = {
                'page_obj': page_obj,
                'blog_latest': blog_latest,
                # 'category': category,
                'categorias_menu':categorias_menu,
                'categorys_tag':categorys_tag,
                # 'comments': comments,
                # 'totalcomments': totalcomments
                }
    return render(request, "blog/blogs.html", content)

# categorys = Category.objects.all()

def blog_detail(request, id, slug):
    categorias_menu = Category.objects.order_by('title')  # transformando meu menu em dinâmico
    categorys_tag = Category.objects.all()
    blogdetails = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post_id=id, status='Lido')
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    # for c in comments:
    #     print('Comentários ::::::::::::::::::', c['comment'])
    # totalcomments = Comment.objects.filter(post_id=id, status='Lido').count()
    # outro jeito de contar os comentários
    totalcomments = 0
    for i in comments:
        totalcomments += 1
    context = {'blogdetails': blogdetails,
               'comments': comments,
               'totalcomments': totalcomments,
               'blog_latest': blog_latest,
               'categorys_tag': categorys_tag,
               'categorias_menu':categorias_menu,
               }

    return render(request, 'blog/blogdetail.html', context)


def add_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.email = form.cleaned_data['email']
            data.post_id = id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

# def category_laravel(request):
#     category = Post.objects.filter(category_id=1) # categoria do Laravel
#     blog_latest = Post.objects.order_by('id')[:6]  # Aqui estou montanto o meu conteúdo para a página e apenas 6 últimos
#     categorys = Category.objects.all()
#     return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})
# def category_django(request):
#     category = Post.objects.filter(category_id=2) # categoria do DJANGO
#     blog_latest = Post.objects.order_by('id')[:6]  # Aqui estou montanto o meu conteúdo para a página e apenas 6 últimos
#     categorys = Category.objects.all()
#     return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})
# def category_mysql(request):
#     category = Post.objects.filter(category_id=3) # categoria do MYSQL
#     blog_latest = Post.objects.order_by('id')[:6]  # Aqui estou montanto o meu conteúdo para a página e apenas 6 últimos
#     categorys = Category.objects.all()
#     return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})
# def category_python(request):
#     category = Post.objects.filter(category_id=4) # categoria do PYTHON
#     categorys = Category.objects.all()
#     blog_latest = Post.objects.order_by('id')[:6]  # Aqui estou montanto o meu conteúdo para a página e apenas 6 últimos
#     # TODO: tentando monstrar os comentários
#     # total = Comment.objects.filter(post_id=id, status='Lido').count()
#     context ={'category': category,
#               'blog_latest': blog_latest,
#               'categorys': categorys,
#               # 'totalcomments': totalcomments,
#     }
#     return render(request, 'blog/categorys.html', context)
# def category_vulnerabilidades(request):
#     category = Post.objects.filter(category_id=5) # categoria do VULNERABILIDADES
#     blog_latest = Post.objects.order_by('id')[:6]  # Aqui estou montanto o meu conteúdo para a página e apenas 6 últimos
#     categorys = Category.objects.all()
#     return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})
