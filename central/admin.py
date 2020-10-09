from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    # Com o argumento {'slug': ('title',)} para a variável prepopulated_fields se está querendo que para o campo slug
    # - seja automaticamente preenchido a partir do title, mas trocando os espaços por traço e talvez removendo algumas
    # - palavras; acentos também são removidos.
    prepopulated_fields = {'slug': ('title',)}
