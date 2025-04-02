from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate #??

# Write tests for views, models, and forms


# Can create a new user
class UserCreationTest(TestCase):
        def test_create_user(self):
            user = User.objects.create_user(username='testuser', password='testpassword')
            self.assertEqual(user.username, 'testuser')
            self.assertTrue(user.check_password('testpassword'))

# Users can log in
class UserLoginTest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        def test_user_login(self):
            self.client.login(username='testuser', password='testpassword')
            user = authenticate(username='testuser', password='testpassword')
            self.assertIsNotNone(user)
            self.assertEqual(user.username, 'testuser')

# Two users cannot have the same username

# Two users cannot have the same email?

# People cannot sign in without creating an account

# Something with logout

