from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class BlogCategory(models.Model):
    category = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User)
    likes = models.IntegerField(default=0)
    slug = models.CharField(blank=True, max_length=150)
    category = models.ForeignKey(to=BlogCategory, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    type = models.IntegerField(default=0)
    parent = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
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
    type = models.IntegerField(default=0)  # Post is 0, comment is 1, child comment is 2
    parent = models.IntegerField()

    def __str__(self):
        return self.author.first_name
