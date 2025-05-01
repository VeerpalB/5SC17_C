from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

ROLE_CHOICES = [ # Done by Veerpal
    ('engineer', 'Engineer'),
    ('teamleader', 'Team Leader'),
    ('department_leader', 'Department Leader'),
    ('seniormanager', 'Senior Manager'),
    ('admin', 'Admin'),
]

class CustomUserCreationForm(UserCreationForm): # Done by Veerpal
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, required=True)
    
    class Meta: # Done by Veerpal
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role']