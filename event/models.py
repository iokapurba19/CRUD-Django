from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title