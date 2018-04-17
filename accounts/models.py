import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from campus.models import School
from social.models import FeedPost
from zones.models import Zone, Area

degree_class = (
    ('1', 'First Class'),
    ('2', 'Second Class Upper'),
    ('3', 'Second Class Lower'),
    ('4', 'Third Class'),
    ('5', 'Pass'),
)


def get_sentinel_user():
    return User.objects.get_or_create(username='deleted')[0]


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile', primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    gradYear = models.CharField(max_length=4, blank=True)
    gradDegreeClass = models.CharField(max_length=50, blank=True, choices=degree_class)
    course = models.CharField(max_length=50, blank=True)
    area = models.ForeignKey(Area, blank=True, null=True)
    zone = models.ForeignKey(Zone, blank=True, null=True)
    resAddr = models.TextField(blank=True)
    resState = models.CharField(max_length=50, blank=True)
    permAddr = models.TextField(blank=True)
    permState = models.CharField(max_length=50, blank=True)
    phone1 = models.CharField(max_length=13, blank=True)
    phone2 = models.CharField(max_length=13, blank=True)
    picture = models.ImageField(upload_to='user-images', blank=True, default='defaults/no-image.png')
    fbProfile = models.URLField(default='http://facebook.com', blank=True)
    twProfile = models.URLField(default='http://twitter.com', blank=True)
    lnkProfile = models.URLField(default='http://linkedin.com', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def follower_count(self):
        return UserFollowing.objects.filter(follows=self.user).count()

    def following_count(self):
        return UserFollowing.objects.filter(user=self.user).count()

    def posts_count(self):
        return FeedPost.objects.filter(user=self.user).count()


class CoordinatorProfile(models.Model):
    user = models.OneToOneField(User, related_name='coord_profile', on_delete=models.CASCADE)
    job_description = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True)
    area_or_zonal = models.IntegerField(blank=True)  # 0 is area, 1 is zonal
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to='coord-picture', default='defaults/no-image.png')

    def __str__(self):
        return self.user.username


class ExcoProfile(models.Model):
    user = models.OneToOneField(User, related_name='exco_profile', on_delete=models.CASCADE)
    job_description = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True)
    area_or_zonal = models.IntegerField(default=0, blank=True)  # 0 is area, 1 is zonal
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to='exco-picture', default='defaults/no-image.png')

    def __str__(self):
        return self.user.username


class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='role')
    role = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1}'.format(self.user.username, self.role)


@receiver(post_save, sender=UserRole)
def create_profile_according_to_role(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.role == 0:
            MemberProfile.objects.create(user=instance.user)
        elif instance.role == 1:
            CoordinatorProfile.objects.create(user=instance.user)
        elif instance.role == 2:
            ExcoProfile.objects.create(user=instance.user)


class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s follows %s" % (self.user.first_name, self.follows.first_name)


class AccountCreationTokens(models.Model):
    token = models.UUIDField()
    role = models.PositiveIntegerField(default=0)
    valid = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.token


# Useful Methods/Functions

def create_profile(user, role=0):
    if role == 0:
        MemberProfile.objects.create(user=user)
    if role == 1:
        CoordinatorProfile.objects.create(user=user)
    if role == 2:
        ExcoProfile.objects.create(user=user)


def create_account_creation_token(creating_user, role):
    if role == 0:
        a = AccountCreationTokens.objects.create(token=uuid.uuid4(), created_by=creating_user, role=0)
        return a.token
    if role == 1:
        a = AccountCreationTokens.objects.create(token=uuid.uuid4(), created_by=creating_user, role=1)
        return a.token
    if role == 2:
        a = AccountCreationTokens.objects.create(token=uuid.uuid4(), created_by=creating_user, role=2)
        return a.token

