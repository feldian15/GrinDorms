# GrinDorms
Repository for GrinDorms CSC 324 project

### Prerequisites
To run this project locally, ensure you have:
- **Python 3** installed
- **Django** installed ('pip install django')
- **Git** installed (for managing version control)

## Instructions to run the system
1. Clone this repo in VSCode
2. Navigate to the GrinDormsDev branch
3. Open the VSCode terminal
4. Run in the terminal (to initialize a virtual environment):\
     python3 -m venv .venv\
     source .venv/bin/activate
5. Open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the Python: Select Interpreter command. From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv
   ![image](https://github.com/user-attachments/assets/9eb6e5e1-b0b9-4c3a-acd1-126cf8ae6b47)
6. In the terminal, run these series of commands:\
     python -m pip install --upgrade pip\
     python -m pip install django\
     pip install python-dotenv\
     pip install django-environ\
     python -m pip install Pillow
7. In the GrinDorms folder, add a .env file with necessary information to run the email backend. **(instructor note: this information was sent to you in an email)**
8. To access the database to delete users created during testing:
   In the terminal, run:\
       python manage.py createsuperuser\
   Choose a username, click enter, click enter to skip email address, enter password
9. Finally, to run the app, in the terminal run:\
      python manage.py runserver\
   click the link generated in the terminal.
**Note: Email functionality does not work on Grinnell Wifi, but works on a hotspot**

## Functional Use Cases
All use cases outlined in the sprint 3 requirements document should be functional EXCEPT for administrators removing flagged content. Currently there is no flagging option for reviews. Also, the account verification process is currently only working on one team-member's computers, so that might not work either. 

## Instructions to test the system:
1. Follow steps 1-8 on running the system.
2. Type "python manage.py test" to test the project.

## Project Description
GrinDorms is an online platform designed to help Grinnell College students browse and contribute dorm room information. Students can search for specific dorms, upload room details, add photos, leave reviews, and compare different rooms based on various attributes (e.g., location, floor). The platform aims to provide a centralized resource for students making housing decisions. 

## Trello Issue Board
We use Trello to track development tasks and manage product progress. You can view open issues, completed tasks, and sprint planning at:
[GrinDorms Trello Board](https://trello.com/b/fiZwfAwq/grindorms)

## Developer Notes:

### Coding Guidelines
We adhere to HackSoftware's Django's coding style guidelines, following the clear rules for writing templates, views, models, and test cases, ensuring maintainable and clean code throughout the project. HackSoftware's documentation expands upon [Django's official style guidelines](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style), but we feel that Hacksoftware's guidelines are better suited for our goals and understanding: [HackSoftware's Django Coding Style Guidelines](https://github.com/HackSoftware/Django-Styleguide?tab=readme-ov-file#overview)

### Testing protocol
To add a new test to the project, use the tests.py file contained in any of the django project apps. Create a testing class that inherits the TestCase class, and create testing functions with names that start with "test_". Then, run `python3 manage.py test` in the project directory, and the tests will run automatically. Additionally, any commit to the GitHub will automatically run the tests in GitHub actions. Currently, only tests in the GrinDormsDemo app will be run automatically. For an example test, look in Demos/GrinDormsDemo/browse/tests.py.

## Contents
### GrinDormsDemo
The directory titled GrinDormsDemo is a localhost site that contains a simple play-around for how a UI might work for our project. To use the demo, navigate to the folder in a terminal, and use the following command line prompt: (Assuming python has been installed on the device)

`python3 manage.py runserver`

This will print a url:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 13, 2025 - 19:14:45
Django version 5.1.6, using settings 'grindormsdemo.settings'
Starting development server at http://000.0.0.0:0000/
Quit the server with CONTROL-C.
```

Copy the server link and add `home/` at the end to get to the homepage

### Written-Reports
The directory titled Written-Reports contains any written reports for class submission, including sprint reports and sprint review reports. 

### djangotutorial
This directory contains a basic Django walkthrough using Python. It includes fundamental concepts and example code to help new developers familiarize themselves with Django.
