# Process Description

### Software Architechure
We will outline two decisions made during this sprint and describe out process in selecting our chosen option.
1) We chose to use Reclaim Cloud
  - We considered using Amazon Web Services (AWS) and a Content Delivery Network, but due to cost and the fact that the college provides hosting through Reclaim, we decided to use the tools provided and work around the limitations of the hosting platform
2) We chose to use Postgres
  - We considered multiple options, for one, a no-SQL database called Couchbase, the default builtin Django SQLite, and lastly Postgres. We ended up using Postgres due to industry norms, ease of finding information on using it, flexibility, and database speed.

### Risk Assessment:
1. One of the main risks of successfully completing our project is not figuring out how to correctly host our website on the reclaim cloud environment that Grinnell set up for us.
- There is a medium likelihood that this will occur, as the person who set up the environment is unable to help up with specific implementation details and there is not a lot of information on how to host via reclaim cloud, vs other cloud hosting services like AWS. The impact if this happens is pretty high, as we will not be able to make our website publicly available. We have tried to navigate the reclaim cloud platform and have found it confusing and unintuitive so far, and we do not have a plan to integrate our project into the cloud environment. If another group is going this route to host a website, we would like to contact them and try to collaborate and learn together. If we are unable to figure out how to host on this platform, we need to identify another free way for us to make our website publicly available.
2. Another risk is that not enough people will use our platform to post room reviews. Even if we do complete our project, we still need a significant number of room reviews for it to be the most helpful to people, as our test users all said that they are most interested in seeing pictures of the inside of dorm rooms. 
- There is a medium likelihood of this occurring, as our platform needs to be complete for users to begin posting reviews, so there is a time constraint and a limited window for people to post reviews once we have completed our project. The impact of this issue is fairly low, as our platform will still function and provide some helpful information about dorm options and help people narrow down their options when selecting a room. We, as a group, will supply as many room reviews as we can from our own accounts and also ask people we know to contribute. It is possible that we can start populating our database before our website is finalized. We can also help users by adding a feature to search specifically for all rooms that do have reviews. 
3. The final risk is if we cannot figure out how to store image data from reviews.
  - the liklihood of this issue occuring is low, since image data is extemely prevalent on the web. We aren't doing anything new, so there should be resources to figure this issue out. If this issue did occur, our functionality would be limited, since seeing the dorm rooms is a primary purpose of our site. Users could still see reviews, but they would lack the ability to actually see the living space. Since image uploading is a common tool on the web, we assume that this will be a straightforward process, even though it is less intuitive than storing text. There are several tutorials we have found that explain how to store image data in databses with django, and it is likely that we can find an answer from these. We are beginning to test these solutions and experiment with test image uploads, which will hopefully lead us to a solution. To detect issues, we will examine the reviews posted to the site and see if the images we test uploads with appear on the page. If not, then we know we haven't solved the problem yet. If for some reason we cannot find a solution to this problem, we would pivot to removing image upload support.


### Epics:
##### Epic 0: Database population
- Description: This epic will populate the room and building databases with all existing rooms and buildings on campus. Full completion is necessary for full functionality, but this does not need to be completed for testing purposes.
- Dependencies: None
- Effort: Likely 1-2 person weeks
- Subtasks: Inputing all building information, inputing all room information

##### Epic 1: User Authentication
- Description: This epic will allow users to create an account with a Grinnell Email, register the account, and log in with an existing account. Once logged in, this epic will keep track of the active account session, for use in other features of the app. There will also be an option to recover an account.
- Dependencies: No requirements, except that there must be some information that is hidden behind the login wall.
- Effort: Likely 2 person weeks to have a functional product
- Subtasks: User database configuration Creating a user view to log in, blocking the site from access without a login, email verification, password recovery, normal login, and active user session information

##### Epic 2: Browse Functionality
- Description: This epic will allow users to browse the database of rooms and examine the most current information. Users must be able to filter, sort and examine the rooms in the database.
- Dependencies: Must have a database configured and populated with basic room information.
- Effort: Likely 3-4 person weeks.
- Subtasks: Room Database configuration, user filtering ability, user sorting ability, room-specific detail page creation

##### Epic 3: Review Functionality
- Description: This epic will allow users to post reviews of the specific rooms they have lived in and upload pictures.
- Dependencies: Must have epic 2: browse functionality semi completed to allow for viewing of the reviews and linking of reviews to rooms, as well as database updates. Also must have epic 1 completed to associate reviews with users.
- Effort: Likely 3-4 person weeks
- Subtasks: Review Database configuration, image database configuration, stepthrough building, floor, room sorting options, input field setup, backend handling of user input and database updating, success messaging or failure safeguards

##### Epic 4: User Review Editing Capability
- Description: This epic will allow users to view their existing reviews and delete or edit them.
- Dependencies: Epic 3 must be completed in its entirety to ensure any updates are populated in the database and displayed accordingly. Epic 1 must be completed to track which user is currently in the session.
- Effort: Likely 1-2 person weeks
- Subtasks: User review page creation, user tracking, editing interface creation, population of existing review information in the editing interface, deletion functionality, success messaging and failure safeguards, updating of database accordingly.

##### Epic 5: PostgreSQL and Reclaim Integration
- Description: This epic will link the app to a postgres database and host it on reclaim cloud, rather than having a simple local host site.
- Dependencies: All prior epics must be completed
- Effort: Likely 1-2 person weeks
- subtasks: Integrate postgres with django app, host app on reclaim

### Product Roadmap
##### Epic 0
- Start Date: March 28
- Approximate completion: April 9
- Flexible completion: End of semester

##### Epic 1
- Start date: March 13
- Approximate completion: March 28
- Flexible completion date: April 4

##### Epic 2
- Start date: March 6
- Approximate completion: April 4
- Flexible completion: April 8

##### Epic 3
- Start date: March 13
- Approximate completion: April 4
- Flexible completion: April 8

##### Epic 4
- Start date: March 24
- Approximate completion: April 4
- Flexible completion: April 18

##### Epic 5
- Start date: March 28
- Approximate completion: April 11
- Flexible completion: End of semester


# CI Plan
- Test Library: We will be using Django's built in test functionality. Included in every Django app is a testing protocol and test class file called tests.py. Tests are run using the `python3 manage.py test` command. This is what we will use. GitHub actions will be used to automate these tests and will run upon committing any code changes. We chose this testing protocol and CI service because they are easily set up and are mostly preconfigured for us to use. The ease of use is a major selling point.



