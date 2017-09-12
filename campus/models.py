from django.db import models


# Create your models here.
class School(models.Model):
    name = models.TextField()
    abbr = models.CharField(max_length=50, blank=True)
    location = models.CharField(blank=True, max_length=50)
    state = models.CharField(blank=True, max_length=50)
    contact = models.CharField(blank=True, max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
