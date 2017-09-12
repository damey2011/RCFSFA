from django.contrib import admin

# Register your models here.
from blogs.models import Like, ChildComment, Comment, BlogPost, BlogCategory

admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(ChildComment)
admin.site.register(Like)