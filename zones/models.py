from django.db import models


# Create your models here.
class Zone(models.Model):
    state = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.state


class Area(models.Model):
    parent_zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    area = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.area
