from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Projects

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User(first_name = 'John', last_name = 'Doe', username = 'test', email = 'test@gmail.com', password = 'nana')
        self.new_user.save()
        self.profile = Profile(prof_pic = 'test.jpg', bio = 'Test bio', phone_number = '0123456789')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    # Testing the save method
    def test_save_method(self):
        self.profile.save_profile()
        details = Profile.objects.all()
        self.assertTrue(len(details) > 0)
