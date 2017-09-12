from django.contrib import admin

# Register your models here.
from forums.models import Thread, Comment, ChildComment, Like

admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(ChildComment)
admin.site.register(Like)
