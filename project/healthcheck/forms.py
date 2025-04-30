from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

ROLE_CHOICES = [
    ('engineer', 'Engineer'),
    ('teamleader', 'Team Leader'),
    ('departmentleader', 'Department Leader'),
    ('seniormanager', 'Senior Manager'),
    ('admin', 'Admin'),
]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    
class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'role']


        