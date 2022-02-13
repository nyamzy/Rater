from django.db import models

# Create your models here.
class Profile(models.Model):
    prof_pic = models.ImageField(upload_to = 'projetcs/')
    bio = models.CharField(max_length=200, null = True)
    phone_number = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.bio
    
    # Save method
    def save_profile(self):
        self.save()

    # 


class Projects(models.Model):
    title = models.CharField(max_length=30)
    landing_page = models.ImageField(upload_to = 'projects/')
    description = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
