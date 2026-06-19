from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)        # Event ka naam
    date = models.DateField()                      # Event ki date
    location = models.CharField(max_length=200)    # Event ka location
    description = models.TextField(blank=True)     # Optional description

    def __str__(self):
        return f"{self.name} ({self.date})"
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Event link
    name = models.CharField(max_length=100)                     # Participant ka naam
    email = models.EmailField()                                 # Participant ka email
    registered_at = models.DateTimeField(auto_now_add=True)     # Auto timestamp

    def __str__(self):
        return f"{self.name} registered for {self.event.name}"
