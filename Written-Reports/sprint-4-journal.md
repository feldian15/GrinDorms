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

## TODO: External Documentation and Stakeholder Meetings
FOR EACH MEETING:
- Who you met with
- Name, occupation, and other relevant information about the stakeholder
- Date and time of the stakeholder meeting
- Description of the test session and feedback
- What was their behavior of interacting with the documentation?
- Did they succeed or get stuck?
- What feedback did they provide about documentation?
- What questions did you ask, and what were the stakeholder's answers?

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

  
## TODO: Self-Selected Work toward Minimum Viable Product (MVP)
- In a Sprint Journal entry, remind us what your MVP is (look back to Milestone 1 where you described what features would be included in your MVP)
- Describe what work, if any, remains toward delivering your MVP

## TODO: Generative AI Experiment
For each use of AI this sprint, write an entry in your Sprint Journal including:
- Name the members of your team who tried it.
- Going into this use of AI, what were your goals and expectations?
- Describe the use specifically in detail. How did you prompt the AI, and what was its output?
- How did this use of AI affect your product development or other sprint deliverables? If you integrated any of its output directly into your code base, include a link to a pull request where the generated output can be clearly distinguished.
- Refer back to your answer to question 2. To what extent did the use of AI achieve your goals and conform to your expectations?
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


