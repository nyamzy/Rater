from .models import Projects
from django import forms

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']
        
