from django.db import models
from django.conf import settings

class Destination(models.Model):
    """Model for representing a place/attraction."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country})"

class Trip(models.Model):
    """A model for representing the entire trip."""
    PRIVACY_CHOICES = [
        ('private', 'Private'),
        ('shared', 'Shared with link'),
        ('public', 'Public'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trips')
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='private')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.owner.username}"

class TripDay(models.Model):
    """A model to represent one day on a trip."""
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='days')
    date = models.DateField()
    day_number = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f"Day {self.day_number} - {self.trip.title}"

class DayDestination(models.Model):
    """Connection between day and places with visiting order."""
    trip_day = models.ForeignKey(TripDay, on_delete=models.CASCADE, related_name='destinations')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.destination.name}"