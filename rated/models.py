from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    prof_pic = models.ImageField(upload_to = 'projetcs/')
    bio = models.CharField(max_length=200, null = True)
    phone_number = models.CharField(max_length=20, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)


    def __str__(self):
        return self.bio
    
    # Save method
    def save_profile(self):
        self.save()

    # Delete method
    def delete_profile(self):
        self.delete()


class Projects(models.Model):
    title = models.CharField(max_length=30)
    landing_page = models.ImageField(upload_to = 'projects/')
    description = HTMLField()
    link = models.URLField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title
    
    # Save method
    def save_project(self):
        self.save()

    # Delete method
    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(title__icontains = search_term)
        return projects

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null = True)
    design_rating = models.IntegerField(default=0, blank = True, null = True)
    usability_rating = models.IntegerField(default=0, blank = True, null = True)
    content_rating = models.IntegerField(default=0, blank = True, null = True)
    average = models.IntegerField(default=0, blank = True, null = True)

    def __str__(self):
        return self.project

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    @classmethod
    def get_project_rates(cls):
        return cls.objects.get_or_create()
          