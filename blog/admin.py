from blog.models import Post
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ("image", "title", "description")
    search_fields = ["title"]


admin.site.register(Post, PostAdmin)
