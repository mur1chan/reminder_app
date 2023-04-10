from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.title