from django.db import models

# Create your models here.

class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    remind_via = models.CharField(max_length=50)  # SMS, Email, etc.

    def __str__(self):
        return f"Reminder at {self.date} {self.time}: {self.message}"
