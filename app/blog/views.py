from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# My Views Creates
from .models import Post, Category, Comment
from .forms import CommentForm


# Create your views here.
def indexblog(request):
    blog_slide_random = Post.objects.order_by('?')[:4]  # Aqui estou montando o SLIDE de forma randomica  e com apenas 4
    blog_latest = Post.objects.order_by('id')[:8]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    categorys = Category.objects.all()
    conteudo = {
                'blog_slide_random': blog_slide_random,
                'blog_latest': blog_latest,
                'categorys': categorys,
                }
    return render(request, "blog/bloghome.html", conteudo)

def categoryLaravel(request):
    category = Post.objects.filter(category_id=1) # categoria do Laravel
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    categorys = Category.objects.all()
    return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})


def categoryDjango(request):
    category = Post.objects.filter(category_id=2) # categoria do DJANGO
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    categorys = Category.objects.all()
    return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})


def categoryMysql(request):
    category = Post.objects.filter(category_id=3) # categoria do MYSQL
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    categorys = Category.objects.all()
    return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})


def categoryPython(request):
    category = Post.objects.filter(category_id=5) # categoria do PYTHON
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    categorys = Category.objects.all()
    return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})


def categoryVulnerabilidades(request):
    category = Post.objects.filter(category_id=6) # categoria do VULNERABILIDADES
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    categorys = Category.objects.all()
    return render(request, 'blog/categorys.html', {'category': category, 'blog_latest': blog_latest, 'categorys': categorys})


def blogs(request):
    blogs = Post.objects.all()
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    category = Category.objects.all()

    paginator = Paginator(blogs, 3)  # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    conteudo = {
                 'page_obj': page_obj,
                 'blog_latest': blog_latest,
                 'category': category,
                }
    return render(request, "blog/blogs.html", conteudo)


def blogDetail(request, id, slug):
    blogdetails = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post_id=id, status='Lido')
    totalcomments = Comment.objects.filter(post_id=id, status='Lido').count()
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    categorys = Category.objects.all()

    return render(request, 'blog/blogdetail.html', {'blogdetails': blogdetails, 'comments': comments, 'totalcomments': totalcomments, 'blog_latest': blog_latest,
                                                    'categorys': categorys})


def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.post_id = id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

