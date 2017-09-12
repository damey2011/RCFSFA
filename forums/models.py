from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse

from rcfsfa.settings import CURRENT_SERVER_HOST


class Thread(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    content = models.TextField()
    isCommentEnabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_comments_count(self):
        return Comment.objects.filter(parent=self.id).count()

    def get_comments_url(self):
        return "%s%s" % (CURRENT_SERVER_HOST, reverse('thread-comments', kwargs={'pk': self.id}))

    def get_like_count(self):
        return Like.objects.filter(type=0, parent=self.id).count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_comments')
    content = models.TextField()
    parent = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username

    def get_comments_count(self):
        return ChildComment.objects.filter(parent=self.id, parent_type=1).count()

    def get_comments_url(self):
        return "%s%s" % (CURRENT_SERVER_HOST, reverse('comments-children', kwargs={'parent_id': self.id}))

    def like_count(self):
        return Like.objects.filter(type=1, parent=self.id)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    type = models.IntegerField(default=0)  # Thread is 0, comment is 1, child comment is 2
    parent = models.IntegerField(blank=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.author.username


parent_types = (
    (1, 'comment'),
    (2, 'child_comment')
)


class ChildComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child_comments')
    content = models.TextField()
    parent_type = models.IntegerField(choices=parent_types, default=1)
    parent = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username

    def get_comments_count(self):
        return ChildComment.objects.filter(parent=self.id, parent_type=2).count()

    def get_comments_url(self):
        return "%s%s" % (CURRENT_SERVER_HOST, reverse('children-children', kwargs={'parent_id': self.id}))

    def like_count(self):
        return Like.objects.filter(type=2, parent=self.id)

