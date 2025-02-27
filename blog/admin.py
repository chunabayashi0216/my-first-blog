from django.contrib import admin
from .models import Post, Comment  #追加


admin.site.register(Post)
admin.site.register(Comment) #追加