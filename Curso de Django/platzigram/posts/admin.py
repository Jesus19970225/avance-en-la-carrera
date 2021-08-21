from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts Admin model"""

    list_display = ('id', 'user','title', 'photo')
    list_display_links = ('id', 'user')
    list_editable = ('photo',)
    list_filter = ('created', 'modifed')

