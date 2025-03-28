from django.contrib import admin
from .models import Articles


# Register your models here.
@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('name',)
