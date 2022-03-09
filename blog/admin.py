from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'content', 
                    'created_on',
                    'author')
    list_filter = ('title',
                    'content', 
                    'created_on',
                    'author')
    search_fields = ['title',
                    'content', 
                    'created_on',
                    'author']

admin.site.register(Post, PostAdmin)