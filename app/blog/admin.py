from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug','created_at']
    prepopulated_fields = {'slug':('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ['status_post', 'title', 'category', 'dt_publicado_em','created_at', 'updated_at']
    prepopulated_fields = {'slug':('title',) }
    readonly_fields = ('image_admin', )
    list_filter = ['status_post','category']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status', 'post','created_at']
    list_filter = ['status','created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
