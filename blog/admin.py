from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'category','date_time')
    list_filter = ('date_time',)
admin.site.register(Article, ArticleAdmin)
