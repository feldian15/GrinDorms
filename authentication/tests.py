from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import CreateUserForm

# Can create a new user (tests the database)
class UserCreationTest(TestCase):
        def test_create_user(self):
            user = User.objects.create_user(username='testuser', password='testpassword')
            self.assertEqual(user.username, 'testuser')
            self.assertTrue(user.check_password('testpassword'))

# Users can log in
class UserLoginTest(TestCase):
        def test_user_login(self):
            self.user = User.objects.create_user(username='testuser', password='testpassword')
            self.client.login(username='testuser', password='testpassword')
            user = authenticate(username='testuser', password='testpassword')
            self.assertIsNotNone(user)
            self.assertEqual(user.username, 'testuser')

# Cannot create a user with the same username as an existing user (tests the database)
class DuplicateUsernameTest(TestCase):
        # Create first user
        def no_dup_username(self):
            User.objects.create_user(username='testuser', password='password123')

            # Try to create another user with the same username
            with self.assertRaises(ValidationError):
                user = User.objects.create_user(username='testuser', password='password123')
                user.full_clean()

# Cannot create a user using a non-Grinnell email (tests the form)
class NonGrinEmail(TestCase):
    def test_invalid_email(self):
        # Create an invalid email
        data = {'email': 'fake@notgrinnell.com'}
        form = CreateUserForm(data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

# Cannot create a user with the same email as an existing user
class DupEmail(TestCase):
    def test_duplicate_email(self):
        User.objects.create_user(username='testuser', password='password123', email='email@grinnell.edu')
        # Create an invalid email
        data = {'email': 'email@grinnell.edu'}
        form = CreateUserForm(data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


# Future changes:
# - (after email verification functionality) try to have a user sign in without an active account
