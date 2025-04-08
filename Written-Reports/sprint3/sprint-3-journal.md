# Sprint 3 Journal
Note: Our requirements document did not change this sprint.

## Testing
The login functionality of our project uses both automated and manual testing. The automated tests handle backend cases,
such as testing whether two users can be created with the same username/email, testing whether an inactive account can login
to the website, etc. Since our app sends verification emails to Grinnell email accounts, it is necessary to test other
functionality manually. For example, testing what happens when users go to their email and click the verification link,
and testing an end-to-end registration process where users create an account, activate it, sign in, and sign out 
(via the sign-out link on the page or by closing their browser window). Additional tests are in place to test the backend integrity of the models and model functions, as well as integration tests between frontend and backend components. We are still currently writing some integration tests using selenium, but these will be active soon. To test the system, simply run the command `python3 manage.py test`. This will execute all tests in all apps. If you want to run only the tests on a particular app, run the command `python3 manage.py test APPNAME`. Run these commands in the main directory, titled 'GrinDorms'. Do not run them in the internal 'GrinDorms' directory (i.e. the path GrinDorms/GrinDorms'. This path houses app configuration information. Ensure the directory includes the manage.py file.
## Building
To build the project on your local machine and run the demo version of the application, clone the repository and run the command `python3 manage.py runserver` from the main 'GrinDorms' directory (Again, not in the internal one). This will produce a message with a localhost url. Ctrl click this link or paste it into a browser to access the login page. From here you can proceed in accessing the site. From here, refer to the readme on how to proceed in using the site.

## Non-user-facing progress
We have made progress in building the full room inventory on campus manually. This will continue throughout the semester.

## Git Tag
The git tag for the in class demo is GrinDormsClassDemo


