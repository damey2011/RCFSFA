from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from campus.models import School

degree_class = (
    ('1', 'First Class'),
    ('2', 'Second Class Upper'),
    ('3', 'Second Class Lower'),
    ('4', 'Third Class'),
    ('5', 'Pass'),
)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='studentProfile', primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True)
    gradYear = models.CharField(max_length=4, blank=True)
    gradDegreeClass = models.CharField(max_length=50, blank=True, choices=degree_class)
    course = models.CharField(max_length=50, blank=True)
    resAddr = models.TextField(blank=True)
    resState = models.CharField(max_length=50, blank=True)
    permAddr = models.TextField(blank=True)
    permState = models.CharField(max_length=50, blank=True)
    phone1 = models.CharField(max_length=13, blank=True)
    phone2 = models.CharField(max_length=13, blank=True)
    picture = models.ImageField(upload_to='user-images', blank=True)
    fbProfile = models.URLField(default='http://facebook.com', blank=True)
    twProfile = models.URLField(default='http://twitter.com', blank=True)
    lnkProfile = models.URLField(default='http://linkedin.com', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
