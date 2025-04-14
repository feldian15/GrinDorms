# Sprint 4 Journal

## Internal Documentation Lab

For each subgroup:
- Name the members of that subgroup
- Identify the code that you worked with in the lab (e.g. calico.java, lines 1-437)
- Write a paragraph to describe the changes that you made to the code and the documentation
- Identify existing documentation that was helpful
- Identify the commit hash of the commit in which you wrote your new documentation. Provide a Github link where your instructor can view the diff of that commit.
- If you created or updated any issues in your issue tracker, show a "before" and "after" snapshot of the detailed view of each issue so that the difference can clearly be seen

### Link to gitdiff of documentation
[gitdiff of Squash-Merge](https://github.com/feldian15/GrinDorms/commit/79ed6aa259cfe02ab9062a581da04baad15b008c)

### Rene & Tim
#### Code
- 'rooms_details.css', 'rooms_home.css', 'my_reviews.css'
- To improve the readability and maintainability of the CSS code, I added a comment before every @media rule across all .css files. The comment explains that the media queries apply specific styling changes when the browser window is resized to a lower resolution, based on the pixel value defined in the media parameter. This documentation helps clarify the purpose of the media query for future developers or team members, indicating that the specified elements (such as headings, fieldsets, and images) will adapt their layout and styling dynamically for smaller screen sizes.
- there are some useful comments like the "general style","link style", and "global page layout" etc. that help explaining the styling function.


### Ian and Mac
##### Code worked with: 
- review/views.py and review/templates/review/review.html(They go together), and browse/models.py
##### Changes: 
- We made changes to the commenting in the review view in the views.py file. Originally, there was not any documentation on what the code was doing, nor was there any description of how the selected options were being used in the template. We added in line comments describing the purpose of each section of code in the view and a description of the way the selected options were passes. Additionally, we updated the building class to add a function that displayed the correct version of the building name. In our database, the buildings are stored as the name in all caps, but on the page we want to display it as titlecased with the word “Hall” appended. We solved this by adding a class method and updated the review html accordingly. We still need to make the same changes in other html templates that display building names. Additionally, we updated the review page to make the rating field a visual star as opposed to text options.
##### Existing documentation: 
The only existing documentation was a brief description of what the view was doing. There was not enough listed to get a good grasp right away.
