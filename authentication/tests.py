from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your tests here.
class UserCreationTest(TestCase):
        def test_create_user(self):
            user = User.objects.create_user(username='testuser', password='testpassword')
            self.assertEqual(user.username, 'testuser')
            self.assertTrue(user.check_password('testpassword'))

class UserLoginTest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        def test_user_login(self):
            self.client.login(username='testuser', password='testpassword')
            user = authenticate(username='testuser', password='testpassword')
            self.assertIsNotNone(user)
            self.assertEqual(user.username, 'testuser')

