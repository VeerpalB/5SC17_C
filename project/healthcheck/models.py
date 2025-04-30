from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

ROLE_CHOICES = [
    ('engineer', 'Engineer'),
    ('teamleader', 'Team Leader'),
    ('departmentleader', 'Department Leader'),
    ('seniormanager', 'Senior Manager'),
    ('admin', 'Admin'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()