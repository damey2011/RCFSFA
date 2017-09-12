from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from accommodation.models import Accommodation


class Programme(models.Model):
    title = models.CharField(max_length=100)
    invited_guests = models.TextField()
    start = models.DateField()
    end = models.DateField()
    flyer = models.ImageField(blank=True, upload_to='program-flyers')
    venue = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" % (self.title, self.start, self.end)


class ProgramInterestedAttendees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.programme.title)


class ProgrammeAccomodationBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    no_of_people = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s booked %s" % (self.user.username, self.accommodation.name)
