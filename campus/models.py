from django.db import models


# Create your models here.
class School(models.Model):
    name = models.TextField()
    location = models.CharField(blank=True)
    state = models.CharField(blank=True)
    contact = models.CharField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
