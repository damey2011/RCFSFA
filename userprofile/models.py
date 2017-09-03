from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from campus.models import School


class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    gradYear = models.CharField(max_length=4, blank=True)
    gradDegreeClass = models.CharField(max_length=50, blank=True)
    course = models.CharField(max_length=50, blank=True)
    resAddr = models.TextField(blank=True)
    resState = models.CharField(50, blank=True)
    permAddr = models.TextField(blank=True)
    permState = models.CharField(50, blank=True)
    phone1 = models.CharField(15, blank=True)
    phone2 = models.CharField(15, blank=True)
    picture = models.ImageField(upload_to='/user-images', blank=True)
    fbProfile = models.URLField(default='http://facebook.com', blank=True)
    twProfile = models.URLField(default='http://twitter.com', blank=True)
    lnkProfile = models.URLField(default='http://linkedin.com', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
