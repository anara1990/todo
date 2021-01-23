from django.contrib import admin
from .models import ToDo
from .models import Book


admin.site.register(ToDo)

# Register your models here.
admin.site.register(Book)