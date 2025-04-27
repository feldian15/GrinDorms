# Sprint 4 Review Report

- **In your report, describe what work remains toward your MVP and your plans for completing the work.**
- To achieve our MVP, we need to host our website publicly and populate our database with basic information for all rooms on campus.
- For the latter, we plan to split up the work amongst our team to add room data to an excel spreadsheet, which will be then be read by an existing script in our code to fill in our app's database. 
  
**Decribe what you completed this sprint:**
  - We added popups when users submit a review to let them know that the review was successfully submitted and help direct them
    to a new page.
  - In the sign-in and register pages, we added links for redirecting users to the sign-in page to the register page and vice versa
    depending on the user's account status.
  - We added functionality to limit room reviews to one review per person per room.
  - We fixed our email functionality to be case insensitive to improve the account creation and password reset processes. 
  - We added more comments to our code to improve the team's understanding of all components.
  - We now have stars for rating rooms instead of numbers.
  - We made layout changes to the browse rooms and room information pages in order to improve user experience.
    
        These changes include:
              - Condensing the filtering panel
              - Adding additional information displayed about rooms on browse page (like single, double, etc)
              - Putting the images and comments for room reviews side-by-side on each room review page
              - Filling stars based on average the average rating (ex. does not round up to whole stars, fills in stars partially)
- We added timestamps to reviews so users can locate the most up-to-date information.
- We added a logout button on all pages in a standard location to allow users to easily sign out of their accounts from any page.
- We have hidden the homepage, browse, review a room, and view your reviews pages to only be visible when users have logged in with a valid account. If they try to access these urls, they will first be redirected to the login page. 
  
**How has your product improved or progressed from a customer perspective?**
- The above changes improve the user experience for our product and make the information easier to access and visually appealing. 
    
**What progress have you made that is not visible to a common user?**
- We have improved the quality of our code and added comments to make it more understandable.
- Making the email case insensitive (by trimming user input and converting it to lowercase) will probably not be recognized by most users, but is essential for our data storage and password reset process.
- Hiding access to pages before users are logged in will probably not be obvious to most users, but it improves the privacy and safety of our website. 
