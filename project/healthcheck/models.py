from django.db import models

class Vote(models.Model):
    category = models.CharField(max_length=100)
    trend = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    team = models.CharField(max_length=20)

    

    def __str__(self):
        return f"{self.category} - {self.trend} - {self.state}"
