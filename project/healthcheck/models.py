from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Vote(models.Model):
    category = models.CharField(max_length=100)
    trend = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    team = models.CharField(max_length=20)

    
class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model): # Done by Veerpal
    
    
    ROLE_CHOICES = [ # Done by Veerpal
        ('teamleader', 'Team Leader'),
        ('engineer', 'Engineer'),
        ('admin', 'Admin'),
        ('department_leader', 'Department Leader'),
        ('seniormanager', 'Senior Manager'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User) # Done by Veerpal
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='engineer')
    else:
        instance.userprofile.save()

      
      


@receiver(post_save, sender=User) # Done by Veerpal
def save_user_profile(sender, instance, **kwargs):
    # Save the user profile every time the user instance is saved
    instance.userprofile.save()
        

# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     else:
#         instance.userprofile.save()

#     def __str__(self):
#         return f"{self.category} - {self.trend} - {self.state}"

