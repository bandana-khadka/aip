from django.contrib import admin
from book.models import Book,Author

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

# Register your models here.
admin.site.register(Book,BookAdmin)