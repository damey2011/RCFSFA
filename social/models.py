import datetime

import math
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.timezone import utc


class FeedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # the null true was added to make creation easy
    post = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' said ' + self.post

    def get_comments(self):
        return reverse('list-create-feed-comment', kwargs={'pk': self.id})

    def get_comments_count(self):
        return Comment.objects.filter(post=self).count()

    def get_like_count(self):
        return PostLike.objects.filter(post=self).count()


class Comment(models.Model):
    post = models.ForeignKey(FeedPost, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def is_parent(self):
        return self.parent is not None

    def get_children(self):
        return reverse('list-create-comment-comment', kwargs={'post': self.post.id, 'pk': self.id})

    def get_children_count(self):
        return Comment.objects.filter(parent=self).count()

    def get_like_count(self):
        return CommentLike.objects.filter(comment=self).count()


class PostLike(models.Model):
    post = models.ForeignKey(FeedPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Conversation(models.Model):
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='started_conv')
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_2')
    time = models.DateTimeField(auto_now_add=True)


class ConversationReplies(models.Model):
    conv = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    reply = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

    @property
    def period_sent(self):
        time_diff = datetime.datetime.now(utc) - self.time
        if time_diff.days < 1:
            if time_diff.seconds < 60:
                return str(math.floor(time_diff.seconds)) + 's'
            elif 60 <= time_diff.seconds < 3600:
                return str(math.floor(time_diff.seconds / 60)) + 'm'
            elif 3600 <= time_diff.seconds < 5184000:
                return str(math.floor(time_diff.seconds / 3600)) + 'h'
        elif 1 < time_diff.days < 30:
            return str(math.floor(time_diff.days)) + 'd'
        elif time_diff.days == 1:
            return 'Yesterday'
        else:
            return self.time.date()
