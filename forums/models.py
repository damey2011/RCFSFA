from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    isCommentEnabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    type = models.IntegerField(default=0)
    parent = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.first_name


class ChildComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.first_name


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(default=0)  # Thread is 0, comment is 1, child comment is 2
    parent = models.IntegerField()

    def __str__(self):
        return self.author.first_name