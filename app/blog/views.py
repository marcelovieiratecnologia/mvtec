from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# My Views Creates
from .models import Post, Category, Comment
from .forms import CommentForm


# Create your views here.
def indexblog(request):
    blog_slide_random = Post.objects.order_by('?')[:4]  # Aqui estou montando o SLIDE de forma randomica  e com apenas 4
    blog_latest = Post.objects.order_by('id')[:3]  # Aqui estou montanto o meu conteúdo para a página e apenas 3 últimos
    category = Category.objects.all()
    conteudo = {
                'blog_slide_random': blog_slide_random,
                'blog_latest': blog_latest,
                'category': category,
                }
    return render(request, "blog/bloghome.html", conteudo)


def categoryPython(request):
    category = Post.objects.filter(category_id=5) # categoria do PYTHON
    return render(request, 'blog/categorys.html', {'category': category})


def categoryDjango(request):
    category = Post.objects.filter(category_id=2) # categoria do DJANGO
    return render(request, 'blog/categorys.html', {'category': category})


def categoryLaravel(request):
    category = Post.objects.filter(category_id=1) # categoria do Laravel
    return render(request, 'blog/categorys.html', {'category': category})


def categoryMysql(request):
    category = Post.objects.filter(category_id=3) # categoria do MYSQL
    return render(request, 'blog/categorys.html', {'category': category})


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
    comments =  Comment.objects.filter(post_id=id, status='Lido')
    totalcomments = Comment.objects.filter(post_id=id, status='Lido').count()

    return render(request, 'blog/blogdetail.html', {'blogdetails':blogdetails, 'comments':comments, 'totalcomments':totalcomments})


def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    print('1')
    if request.method == 'POST':
        print('2')
        form = CommentForm(request.POST)
        if form.is_valid():
            print('3')
            data = Comment()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.post_id = id
            print(data)
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
