from .models import Author, Book, Genre
from django.contrib import admin

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthdate')
    search_fields = ('name',)
    list_filter = ('birthdate',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    search_fields = ('title', 'author__name')
    list_filter = ('publication_year', 'author')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
