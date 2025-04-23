# Sprint 4 Journal

## Internal Documentation Lab

### Link to gitdiff of documentation
[gitdiff of Squash-Merge](https://github.com/feldian15/GrinDorms/commit/79ed6aa259cfe02ab9062a581da04baad15b008c)

### Rene and Tim
#### Code
- 'rooms_details.css', 'rooms_home.css', 'my_reviews.css'
- To improve the readability and maintainability of the CSS code, I added a comment before every @media rule across all .css files. The comment explains that the media queries apply specific styling changes when the browser window is resized to a lower resolution, based on the pixel value defined in the media parameter. This documentation helps clarify the purpose of the media query for future developers or team members, indicating that the specified elements (such as headings, fieldsets, and images) will adapt their layout and styling dynamically for smaller screen sizes.
- there are some useful comments like the "general style","link style", and "global page layout" etc. that help explaining the styling function.

### Ian and Mac
#### Code worked with: 
- review/views.py and review/templates/review/review.html(They go together), and browse/models.py
##### Changes: 
- We made changes to the commenting in the review view in the views.py file. Originally, there was not any documentation on what the code was doing, nor was there any description of how the selected options were being used in the template. We added in line comments describing the purpose of each section of code in the view and a description of the way the selected options were passes. Additionally, we updated the building class to add a function that displayed the correct version of the building name. In our database, the buildings are stored as the name in all caps, but on the page we want to display it as titlecased with the word “Hall” appended. We solved this by adding a class method and updated the review html accordingly. We still need to make the same changes in other html templates that display building names. Additionally, we updated the review page to make the rating field a visual star as opposed to text options.
##### Existing documentation: 
The only existing documentation was a brief description of what the view was doing. There was not enough listed to get a good grasp right away.

### Ella and Nitin
- views.py in the login app (entire file)
- This file did not have exsiting documentation for functionality accomplished in the code and remaining tasks to complete. We added descriptive in-line comments to detail what each function does and to describe specific lines of code. We added a block comment at the beginning of the document describing the code in general. We also went through and added comments for TODO items, including things we can delete and changes to make the code more consistent throughout.
- We added an issue to the issue tracker for the next step for login, which is to ensure all of the urls in the other app are protected, and redirect users to the login page before being able to access them. This issue is called "Protect web pages" and we were able to successfully make the needed changes to do so. This issue has been moved to the completed section of our Trello board.

## External Documentation and Stakeholder Meetings

### Meeting 1: Kailee Shermak (April 16, 6:14pm)
- This meeting was with Kailee Shermak, a fourth year sociology major with a digital studies concentration at Grinnell College. Kailee is on the swim team and was a test user for our paper prototype. She has lived in various dorms on campus.
- Kailee's interaction with the documentation was limited. She skimmed it beforehand, but said that it was not necessary for her to understand how to navigate the website, and did not refer to it while testing the project. She did not give feedback on the documentation otherwise. 
- Kailee succeeded in the goal of creating and verifying an account, browsing for rooms, and posting room reviews.
  
**Question 1: What aspects of the website did you like?**
- Overall, Kailee enjoyed the aesthetics of the website. 
- She liked the black bar display for each room in the browsing page of our website and also liked the setup of the initial homepage after logging in.
- She said the process for registering and verifying an account was easy, and she liked the email verification aspect of that process.
  
**Question 2: What aspects of the website were confusing/unintuitive?**
- When filtering for rooms in the browse section of the webstite, she thought the apply filters button was hard to navigate to because she had to scroll down a lot. She recommended moving this button to the top of the filtering section.
- Kailee also found part of the review form to be unintuitive. She thinks that if someone goes back to change information about a room (ex. cluster on campus, floor number, etc, it should automatically refresh/remove the information following it, as it would then be incorrect. This happens when users change info and click the next button, but Kailee found this unintuitive and a little clunky.
- When navigating to the review page directly from clicking on a "review this room" button on a room review page, Kailee thinks that users should not have the ability to alter the room/cluster/floor information, and should just be allowed to post a review for that specific room

**Other misc feedback during the test:**
- Kailee thought the inital colors of the stars for the room reviewing form were confusing because they were already green, so she thought it was a default five-star review and didn't know she had to select a star rating. She thinks the starts should start out with a black outline and white center. When she didn't select stars and tried to submit, she was unable to submit and it took her a while to figure out the reason, since there was no error message shown. 
- She thought the room labels "five-man", "six-man", etc should be changed to "five-person," etc.
- She thinks the website should limit image files uploaded to be JPEG and PNG. She tried to upload a PDF and nothing broke, but the image was blank and just showed the name of the image, so users should probaly be prevented from uploading files of an invalid format. 

### Meeting 2: Devon Cuddihy (April 22, 8:00pm)
- This meeting was with Devon Cuddihy, a first-year economics major at Grinnell College. Devon is on the football team and was a test user for our paper prototype.
- Devon's interaction with the website was very breif, as he used it to try and look up room information of dorms that were popular during room draw just to try and gage what each room was like with the details that were presented.
- Devon was able to browse rooms easily, as well as posting a review for the room he currently resides in.

**Question 1: What aspects of the website did you like?**
- Devon really enjoyed the color scheme that was used. He said the blue hover mechanic on the buttons was a nice touch, and the modern/sleek aesthetic was not overwhelming.
- He also enjoyed how simple it was to navigate the website was. He thought it was very intuitive and straight-forward.
- He thought the ability to not only review a room from the home button that is present, but to review a room from the actual room details itself was very convenient, as it removes having to navigate back to the home page and searching for the room through the initial review a room steps.

**Question 2: What aspects of the website were confusing/unintuitive?**
- Devon brought up a similar point to Kailee's that when someone checks a filter, it should automatically do so, instead of having to scroll down and click apply filters, as the rooms are already present on the right-hand side of the filter bar.
- He also said the filter bar is too long, as having to scroll up and down just to see all of the filter options was a hassle for him, as he seemed to get lost. He suggested having a drop down for each filter option, as well as condesning the filter bar as a whole (i.e., not have so much blank space between options, but this could be addressed with the use of drop downs).

**Other misc feedback during the test:**
- Similar to Kailee's interaction, Devon thought the stars in the 'review a room' page where already filled in due to the stars when they are not yet selected to appear green. He tried to submit a review without selecting a star rating. He suggested greying them out to tell users that the stars are not filled out.
- He also suggested that if the users do not select a star rating, a popup should inform users that a star rating is required.

### Meeting #3: Jacob Gaynor (April 22, 1:00pm)
**Question 1: What aspects of the website did you like?**
- Jacob enjoyed the layout of the browsing page. He said it was easy to see the filtering options and rooms side by side instead of in a long list.
- Jacob also like that the reviewing process was straightforward and worked in steps. He said it was easy to understand and find the correct room.
- Jacob commented on the simplicity of the site as a positive. He said he thought the UI was not distracting and made it very straightforward to navigate.

**Question 2: What aspects of the website were confusing/unintuitive?**
- Jacob thought that having the submit button all the way at the bottom of the filtering panel on the browse page was somewhat confusing, as it could be missed for someone who didn't scroll.
- Jacob also commented on the way that images were not able to be enlarged on the room details page.
- Jacob thought that not being able to edit a review and instead having to delete and reupload was a major drawback.

**Other misc feedback during the test:**
- Jacob thought that there should be some way to limit results on the browse page, as having every possible room could be overwhelming.
- He also thought that seeing the type of room on the browse page before selecting it would be helpful. He mentioned that seeing more information as well (Like region, srd status, etc) would also be helpful to see more information across a range of rooms without navigating to a specific one.

## Self-Selected Work toward Minimum Viable Product (MVP)
The MVP described in our Milestone 1 document has the following features:
- Log-in with your student email before viewing any dorm information. 
- A feature to upload information about your own dorm room (photos, star rating, text review, etc.)
- Ability to view a catalogue of all dorm rooms on campus (photos, etc.). These will be static pages that are linked from the home page and from the details of the rooms.
- Ability to remove information at your own discretion (privacy) 
- Ability to view/edit/delete your past reviews
- Add custom sorting and filtering functionality for users to query the room database instead of the flow where users need to click on building, floor, and room.

Almost all of this functionality has been implemented so far. The work that remains is to populate our database with all rooms on campus to allow for reviews/browing functionality for all of the rooms (the third feature). Right now, we have a limited selection of rooms to review/browse. Additionally, we are in the process of working on hosting our website publicly, and making sure the email backend is correctly configured for this new setup, to allow for account verification. 

## TODO: Generative AI Experiment
For each use of AI this sprint, write an entry in your Sprint Journal including:
- Name the members of your team who tried it.
- Going into this use of AI, what were your goals and expectations?
- Describe the use specifically in detail. How did you prompt the AI, and what was its output?
- How did this use of AI affect your product development or other sprint deliverables? If you integrated any of its output directly into your code base, include a link to a pull request where the generated output can be clearly distinguished.
- Refer back to your answer to question 2. To what extent did the use of AI achieve your goals and conform to your expectations?

### Selenium Tests Experiment (Ian and Tim)
1. Our goal in this experiment was to see if ChatGPT could help us create a test user and login to our site so that we could access the full site and run automated integration tests. We expected ChatGPT to be mostly right, since this is a simple task with plenty of examples online.
2. We prompted the AI by first writing: "I am going to give you a couple of html templates and some test functions for a django app. I need help writing a selenium test that is able to login and access login required pages. Please do not write me any code until I tell you what I want written." Then we provided three HTML templates relating to our login page, followed by our existing test code. ChatGPT responded with "Sounds good! Go ahead and share your HTML templates and test functions whenever you're ready, and I’ll follow your lead." After each HTML file, it remained in waiting and prompted us to continue to submit our code. Once we had uploaded all of the necessary code, we used the prompt: "Lets create a test user first, step by step." Chat GPT then respnded with:

Great! To create a test user, you can add this to the setUpClass method in your HomePageTest. Django’s test database is recreated for each test run, so this user will only exist during tests:

from django.contrib.auth.models import User

@classmethod
def setUpClass(cls):
    super().setUpClass()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    cls.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Create a test user
    cls.test_username = "testuser"
    cls.test_password = "testpassword123"
    User.objects.create_user(username=cls.test_username, password=cls.test_password)
This gives you a consistent test user you can use in your Selenium login test. When you're ready, we can move on to the Selenium login step.

  Finally, we had it go step by step through the full login, which it responded to with:

Perfect! Let's break it down step by step.

Step 1: Navigate to the landing page
First, we want to go to the landing page where the user will click on the "Sign-in" link. This is the page you showed earlier.

def login(self):
    # Navigate to the landing page
    self.driver.get(self.live_server_url)
Step 2: Click the "Sign-in" link
Once we're on the landing page, we will find the Sign-in link and click it to go to the login form.

    # Click on the "Sign-in" link
    sign_in_link = self.driver.find_element(By.LINK_TEXT, "Sign-in")
    sign_in_link.click()
Step 3: Wait for the login page to load
After clicking the link, we'll need to wait for the login form to be fully loaded before interacting with the elements.

    # Wait for the login form to be available (e.g., wait for a form element)
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))  # assuming 'username' is a field in the form
    )
Step 4: Fill in the username and password
Next, we'll find the username and password fields and enter the test user's credentials.

    # Find the username and password fields and fill them in
    username_field = self.driver.find_element(By.NAME, 'username')
    password_field = self.driver.find_element(By.NAME, 'password')

    # Fill in the test user's credentials
    username_field.send_keys(self.test_username)
    password_field.send_keys(self.test_password)
Step 5: Submit the form
Once the form is filled out, we’ll find the submit button and click it.

    # Find and click the submit button
    submit_button = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_button.click()
Step 6: Wait for the redirect to the home page
Finally, we'll wait until the login process is complete and the user is redirected to the home page.

    # Wait for the redirection to the home page (or another page that indicates login success)
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be(self.live_server_url + "/home/")
    )
Full Login Function
Here’s the complete function:

def login(self):
    # Navigate to the landing page
    self.driver.get(self.live_server_url)

    # Click on the "Sign-in" link
    sign_in_link = self.driver.find_element(By.LINK_TEXT, "Sign-in")
    sign_in_link.click()

    # Wait for the login form to be available
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )

    # Fill in the username and password
    username_field = self.driver.find_element(By.NAME, 'username')
    password_field = self.driver.find_element(By.NAME, 'password')
    username_field.send_keys(self.test_username)
    password_field.send_keys(self.test_password)

    # Submit the form
    submit_button = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_button.click()

    # Wait for the user to be redirected to the home page
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be(self.live_server_url + "/home/")
    )
With this function, your test is ready to log in the user before checking the homepage.

Let me know when you want to continue and write a test that uses this login function!

3. This use of AI made the process of troubleshooting our broken tests much simpler. Instead of trying to find an example somewhere on the internet and then trying to piece it together in our own code, we were able to give ChatGPT our existing work and have it amend the code with specific details relevant to our project. The hash for the commit is 8ab9025ffb20dd1ee63fac1c68fe340c29f1ddf6. We made a few changes to the code like altering the password and making sure the test user was marked as active, but otherwise, we left the code mostly the same as it was generated.
4. This experiment mostly conformed to our expectations. Since we were very deliberate about asking for specifics in the type of responses, we got easy to understand answers with explanations that made it easy to fix the issue we were having in our tests.

  
### Golden Stars Experiment (Mac)

One issue we had with our code (or goal we had), was to implement a visually appealing rating with golden stars specific to each room. For example, the average room rating would say “4 stars”, and we wanted to create a visual representation of the corresponding amount of stars. I prompted the AI to implement a CSS function that displays the correct corresponding number of golden stars when give an integer as a parameter. It gave me a function that worked as expected. 

This significantly helped our project because stack overflow and other resources did not have any examples of code that worked for our specific format. This has definitely added to my learning because it showed me a new way to use a CSS function to display a visual result. My advice to my peers is to use AI when you are fully stuck, or you have a problem that is specific to your exact project, where limited resources exist online posted by real humans. 


.star-rating {
    display: inline-block;
    font-size: 1.2em;
    color: #ffc107; /* Gold color for stars */
    position: relative;
    unicode-bidi: bidi-override;
    width: 5em;
}

.star-rating::before {
    content: "★★★★★";
    opacity: 0.3;
}

.star-rating::after {
    content: "★★★★★";
    position: absolute;
    left: 0;
    top: 0;
    width: calc(var(--rating) * 1em);
    overflow: hidden;
    opacity: 1;
}

### Email Experiment (Ella)
1. One of the tasks I needed to complete was to ensure that email address input is always case insensitive so the app can sucessfully match an email address to a user's account and send a verification/password reset email. My goal for this AI experiment was to test how AI could help me understand why the code was not currently case insensitive, and how to change the code to complete the task.
2. First, I wanted to figure out what the line of code "self.cleaned_data.get("email")" in my forms.py file was actually doing. I expecting an answer that would indicate that the email string was being altered in some way. 

**Prompt:** "I am working on a login subapp using django. In my forms.py file, I have "self.cleaned_data.get("email")". What does this do to the email entered by the user?"

**Output:** 

...............................................................................

Great question!
In Django forms, self.cleaned_data.get("email") is used after form validation to retrieve the cleaned (i.e., validated and normalized) value of the email field that the user submitted. Here's a breakdown of what it does:

📌 What self.cleaned_data.get("email") Does
self.cleaned_data is a dictionary-like object that holds all the form fields and their cleaned (processed) values after calling form.is_valid().

.get("email") attempts to retrieve the value associated with the "email" field from that dictionary.

So essentially:

python
Copy
Edit
email = self.cleaned_data.get("email")
means: "Give me the email the user entered, but only after it's been validated and cleaned by the form."

🧼 What "cleaned" Means
Django applies a few steps during cleaning:

Validation: It checks if the field satisfies all conditions (e.g., required, proper email format).

Type conversion: It converts the value to the expected Python type (e.g., converting string to datetime, ensuring email is a string in valid format).

Custom clean methods: If you define clean_email(self) in your form, Django will run it and use its return value in cleaned_data.

🚨 Important
This only works after form.is_valid() is called, because cleaned_data doesn’t get populated until then.

...............................................................................

4. This output did not exactly answer what I was trying to figure out. I then asked if that line converted the email to the trimmed, lowercase version. The response what that it did not. I then asked how to accomplish that conversion, and it told me to add .strip().lower() to the line of code. I changed my code based on this advice, and accomplished my goal. (Altered code is in commit 1 for the Cleaned Code pull request (#41).
5. This use of AI affected my product development because it helped me understand what a line of code was doing, and gave me options on how to alter that line of code to accomplish my goal. Once I knew the right questions to ask, it helped me in my product development.
6. Initally, I got an answer I was not expecting and had to rephrase my question in order to get the results I wanted. In general, this use of AI mostly conformed to my expectations and overall helped me achieve my goal more efficiently than I would have by trying to look at documentation or going on Google. 

### Documentation to .css login files (Rene)
One thing I thought that needed to be addressed in our code was the lack of documentation, specifically in our .css files. This is not limited to the 3 files I experimentated on, but I wanted to see how ChatGPT would go about providing comments to the code. I first provided the .css I wanted to be documented (in this case 'index.css'), and then provided the associated .html file that it is being loaded in (in this case 'index.html'). The prompt looked something like this:

*This is 'index.css': [provided code]*

*This is 'index.html': [provided code]*

*Add documentation to the code.*

I thought providing the .html file would provide clarity as to what is exactly being styled. And would thus provide a more accurate and comprehensive comments within the .css files. This is what was provided to me for 'index.css':

...............................................................................

Here is your updated `index.css` file with clear and professional documentation added as comments throughout the file:

```css
/* ============================
    Global Page Layout
   ============================ */

/* 
   Styles for the entire page layout.
   - Centers all content both vertically and horizontally.
   - Uses a clean, readable sans-serif font.
   - Sets a light background and removes default margins.
*/
body {
    background-color: #f0f4f8;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    text-align: center;
}


/* =======================
    Heading Styles
   ======================= */

/*
   Styles the main heading on the page.
   - Increases font size for emphasis.
   - Applies a dark, modern color.
   - Adds spacing below the heading.
*/
h1 {
    font-size: 3em;
    color: #2c3e50;
    margin-bottom: 1em;
}


/* ============================
    Button/Link Styles
   ============================ */

/*
   Styles for all <a> elements acting as buttons.
   - Removes underlines from links.
   - Applies white text on a green background.
   - Adds padding and rounded corners for a button look.
   - Adds smooth transition effect on hover.
   - Adds vertical spacing between buttons.
*/
a {
    text-decoration: none;
    color: white;
    background-color: #2b9533;
    padding: 12px 24px;
    border-radius: 8px;
    transition: background-color 0.3s ease;
    display: inline-block;
    margin: 10px 0;
}

/*
   Hover state for links.
   - Changes background color to a blue tone when hovered over.
*/
a:hover {
    background-color: #2980b9;
}
```

Let me know if you want this broken into separate component-specific files later (e.g., `buttons.css`, `layout.css`, etc.), or want dark mode variants!

...............................................................................

After reviewing the documentation provided, I thought it was very accurate and helpful to understand what exactly is being done in each code block. It definetly exceeded my expectations as to what will be provided. It significantly improved not only my group members understanding of what each block of styling is doing, but even my own understanding, and I wrote most of this code. It definetly was useful in this regard, and it will definetly help improve our own documentation practices moving forward.

**These AI-generated comments can be found in pull request #43, titled: 'login' .css documentation**
