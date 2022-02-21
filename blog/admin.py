from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ("created_on",)
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)