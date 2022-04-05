""" Blog App - admin.py """
from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    """
    Post Admin
    """
    list_display = {'title', 'body', 'image', 'image_url', 'date_added'}
    list_filter = {'date_added'}
    search_fields = {'title', 'body'}
    readonly_fields = ('date_added')

    ordering = ('-date_added')


admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comments Admin
    """
    list_display = ('name', 'body', 'post', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        """
        Set which field should update when a comment is approved
        """
        queryset.update(active=True)
