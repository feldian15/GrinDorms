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

