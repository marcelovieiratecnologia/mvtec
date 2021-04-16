from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug','created_at']
    prepopulated_fields = {'slug':('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ['status_post', 'title', 'category', 'created_at', 'updated_at']
    prepopulated_fields = {'slug':('title',) }
    readonly_fields = ('image_admin', )
    list_filter = ['status_post','category']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status', 'post']
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
