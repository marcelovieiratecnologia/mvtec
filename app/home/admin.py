from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['nome', 'assunto', 'email', 'status', 'created_at']
    list_filter = ['status']



admin.site.register(Contact, ContactAdmin)
