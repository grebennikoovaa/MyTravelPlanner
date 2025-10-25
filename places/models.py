from django.db import models

class Place(models.Model):
    PLACE_TYPES = [
        ('attraction', 'Attractions'),
        ('restaurant', 'Restaurant'),
        ('hotel', 'Hotel'),
        ('shop', 'Shop'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    types = models.CharField(max_length=100, choices=PLACE_TYPES)
    created_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name