from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200, null=False)
    slug = models.SlugField(unique=True, null=False)

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Alterado em', auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'tb_mvt_category'  # definindo o nome da tabela, no caso não utilizei deixei o django fazer por mim
        verbose_name = 'Categoria'  # 'Entrada/Saída'
        verbose_name_plural = 'Categorias'

class Post(models.Model):
    STATUS_POST = (
        ('Publicado','Publicado'),
        ('Não Publicado','Não Publicado'),
        ('Arquivado','Arquivado'),
    )
    status_post = models.CharField(choices=STATUS_POST, max_length=14, default='Não Publicado')
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    title = models.CharField(verbose_name='Título', max_length=200, null=False)
    slug = models.SlugField(unique=True, null=False)
    subtitle = models.CharField(verbose_name='SubTítulo', max_length=200, null=False)
    description = models.TextField(verbose_name='Descrição', null=False)
    image = models.ImageField(verbose_name='Imagem', upload_to='images/', blank=True) # Tamanho : 580x500 px
    # text = models.TextField(verbose_name='Texto', null=False) Passei a usar o CKEDITOR, então mudei conforme a linha abaixo
    text = RichTextUploadingField(verbose_name='Texto')
    fonte = models.CharField(max_length=255, null=True)


    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Alterado em', auto_now=True)


    def image_admin(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return mark_safe('<p>Sem Imagem</p>')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_mvt_post'  # definindo o nome da tabela, no caso não utilizei deixei o django fazer por mim
        verbose_name = 'Blog'  # 'Entrada/Saída'
        verbose_name_plural = 'Blogs'


class Comment(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Não Lido', 'Não Lido'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, blank=False)
    email = models.EmailField(max_length=120, null=False, default=None)
    comment = models.TextField(blank=False)
    status = models.CharField(choices=STATUS, max_length=14, default="Não Lido")

    created_at = models.DateTimeField(auto_now_add=True)

    # def display_category(self):
    #     return ', '.join(post)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_mvt_comment"
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"