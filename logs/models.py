from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ipAddr = models.GenericIPAddressField()

    def __str__(self):
        return "%s logged in from %s at %s" % (self.user.username, self.ipAddr, self.timestamp)
