from django.contrib import admin

from .models import Post, Comment , categories

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(categories)
