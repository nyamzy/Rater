from .models import Profile, Projects
from django import forms

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']