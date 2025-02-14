# Milestone 2 Report

## Work completed by each team member
**Ian:** Set up GitHub and Trello Board and messed around with Django tutorial. Wrote the README. 

**Ella:** Created Written-Reports folder and wrote the Milestone 2 report. Emailed Mo Pelzel to inquire about web hosting options through Grinnell and requested for him to set up a Cloud environment to host the project.  

**Nitin:** Guided group in deciding which technologies (databases, programming languages, etc) are optimal.   

**Mac:** Researched Django and found an online tutorial. 

**Tim:** Created the frontend folder and wrote readme.md and a test program app.py using nicegui 

**Rene:** Expanded upon the READNE.md for further clarity and aesthetics.  


## Important decisions
There were two main routes we considered in the implementation of our project, ultimately choosing to host our website through Grinnell. Initially, we planned to implement our project without the use of Grinnell resources. Had we chosen this path, we identified Django as the main framework to build the website. On the backend, we researched Firebase to store data and manage users, as well as CloudFlare to help with image storing, but this service would be at cost. Based on advice from Professor Perlmutter, we decided to pivot and explore the options that Grinnell provides for hosting websites.  

We contacted Mo Pelzel, the Director of Academic Technology for Grinnell College, who provided two hosting options offered by Grinnell through Reclaim Hosting. The main offering is for projects that can run on the LAMP environment (Linux/Apache/MySQL/PHP), which we decided did not fit our needs. We decided to go with the more specialized web development environment (Reclaim Cloud: https://reclaim.cloud/) which will allow us to work within a container-based server infrastructure and customize our tech stack and resources. With this option, we can still develop using Django in a Docker container but will switch to a MySQL database rather than Firebase. This seems to be our best option, as it is free and Mo can support us in the setup of the Cloud environment. Reclaim Cloud also provides tutorials related to cloud hosting, containers, Docker, and managing environments (https://www.youtube.com/playlist?list=PLpK5svzslv8qNyoW7VsYT9cp0Ht5MhBgl).  

## Programming languages & tools
We plan to develop our website using a Cloud environment offered by Grinnell through Reclaim Cloud. With this option, we will develop in Docker containers using Django and will store our data in a MySQL database. Mo will help us set up the Cloud environment. Once we have access to it, we will be able to better plan our implementation. At this point, we are not sure how we will approach user management. For now, we are watching the tutorials provided by Reclaim Cloud. 

## How we chose these technologies
The main components of our project include user-management based on Grinnell emails, data storage for numeric, text, and image data, and a public website to display and submit room data in a visually appealing way. We initially did research on our own to determine common languages and databases used in web develpment. After consulting Mo from the Digital Liberal Arts Collaborative, we decided to pivot from our original plan of using Firebase to a Cloud environment that provides a MySQL database. 

