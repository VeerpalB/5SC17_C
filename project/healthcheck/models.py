from django.db import models

class HealthCard(models.Model):
    STATUS_CHOICES = [
    'worse', 'getting worse', 
    'stable', 'stable', 
    'improving', 'improving',

    ]

category = models.CharField(max_length=100 )
status = models.CharField(max_length=20, choices=STATUS_CHOICES)
timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.category} - {self.status}"

class HealthCard(models.Model):
    TREND_STATUSES = [
        ('worse', 'Worse'),
        ('getting worse', 'Getting Worse'),
        ('stable', 'Stable'),
        ('improving', 'Improving'),
    ]

    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=TREND_STATUSES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.status}"

    
  
    