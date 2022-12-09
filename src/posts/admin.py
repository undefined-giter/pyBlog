from django.contrib import admin
from posts.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_on', 'last_update')
    list_ediatable = ('published',)

admin.site.register(BlogPost, BlogPostAdmin)