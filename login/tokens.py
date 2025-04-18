### *****************
### tokens.py
### Author: Ella Berman
### Generate the token used to validate user accounts via an emailed link.
### *****************
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return(
            str(user.pk) + str(timestamp) + str(user.is_active)
        )
    
account_activation_token = AccountActivationTokenGenerator()