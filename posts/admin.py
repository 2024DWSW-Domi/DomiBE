from django.contrib import admin
from .models import Post, Category, Day

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Day)