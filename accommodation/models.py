from django.db import models


# Create your models here.
class Accommodation(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    town = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class AccommodationPhotos(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accommodations')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accommodation.name
