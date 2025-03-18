# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post

# assim é como está no tutorial Django Girls
# admin.site.register(Post)

# assim fica mais customizado: a tabela exibe as colunas com seus respctivos campos
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created_date", "published_date")
