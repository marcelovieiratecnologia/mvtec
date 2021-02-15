from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug','created_at']
    prepopulated_fields = {'slug':('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at', 'image_admin']
    prepopulated_fields = {'slug':('title',) }
    readonly_fields = ('image_admin', )
    list_filter = ['category']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
