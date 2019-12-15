from django.contrib import admin
from booktest1.models import Book
from booktest1.models import Hero


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'book_date']


class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'hero_name', 'hero_skill', 'book_id']


admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
