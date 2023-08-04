from django.contrib import admin
from .models import Books


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
    search_fields = ['id', 'title']
