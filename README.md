# **Recip<span style='color:orangered'>ease</span> - AMS CRUD Application** by Denis Hayes

 ## **Introduction**
---
### This project has been completed according to the SFIA Framework, to satisfy the deliverable requested by AMS to assess familiarity/competency with the core concepts that have so far been covered within the QA DevOps training program.

<br>

### The application provides users with a platform on which to host their recipes, share these recipes and browse the recipes uploaded by other users.

<br>

### The application uses the Flask framework in conjunction with a relational SQL database.

<br>

**Read-Only access to the project's Trello board is available here:
https://trello.com/invite/b/KeJbV393/ATTI7cae7677ff9adf76bd7ff788deaa67b80957613D/tasks**

<br>

 ## **Table of Contents**
---

1. [Introduction](#introduction)
2. [Project Aims](#project-aims)
3. [User Stories](#user-stories)
4. [Planning](#planning)
5. [Risk Assessment](#risk-assessment)
6. [Existing Features](#existing-features)
7. [Upcoming Features](#upcoming-features)
8. [Known Issues](#known-issues)
9. [Testing](#testing)
10. [Data Structure](#data-structure)
11. [Site Structure](#site-structure)
12. [Design](#design)
13. [Technologies Used](#technologies-used)
14. [Acknowledgements](#acknowledgements)

 ## **Project Aims**
---
### **The aims of the this project are:**
- To create a fully functional CRUD application.
- To sufficiently test the functionality of the application.
- To utilise supporting tools in the creation of the application.
- To apply the learned methodologies to the development process.
- To fully document the process of the application's design.
<br>

 ## **User Stories**
---
### First Time User
* As a first time user I want to quickly understand the purpose of the website.
* As a first time user I want to be able to navigate the site easily.
* As a first time user I want to be able to view other people's recipes, allowing me to ascertain whether or not this is a community I want to be a part of.
* As a first time user I want to be able to easily Sign Up to the site, should I choose to do so.

### Returning User
* As a returning user I want to be able to quickly and easily Log In to the site.
* As a returning user I want to be able to easily create and update recipes.
* As a returning user I want to be able to delete recipes that I no longer want to display.
* As a returning user I want to be able to easily see all of the recipes that I have created.

 ## **Planning**
---
The development of this project has been carefully planned and executed according to a Trello Board established for this purpose.

Built in Trello features such as labels and descriptions allow for 'at a glance' understanding of tasks and priorities.


**Read-Only access to the Trello board is available here:
https://trello.com/invite/b/KeJbV393/ATTI7cae7677ff9adf76bd7ff788deaa67b80957613D/tasks**

Wireframes created using Balsamiq were used to plan the basic intended layout of the website.

These initial wireframes can be viewed below.

### Index
![](README_Assets/Wireframes/Index.png)

### Log In / Sign Up
![](README_Assets/Wireframes/Log_In_Sign_Up.png)

### Profile
![](README_Assets/Wireframes/Profile.png)

### Create/Update Recipe
![](README_Assets/Wireframes/Create_Update_Recipe.png)

### View Recipe
![](README_Assets/Wireframes/View_Recipe.png)


 ## **Risk Assessment**
---
A thorough risk assessment was performed at the outset of the planning phase, with new risks and mitigating actions being added to it over the course of the project.

Thankfully, none of the documented risks materialised, partially due to luck but predominantly due to careful and meticulous planning and execution. The risk assessment is available within the project files, and an image of the finalised document can be seen below.

### Risk Assessment
![](README_Assets/Risk_Assessment.png)

 ## **Existing Features**
---
### **Navigation Bar**
* A fixed-to-top Bootstrap Navbar, is visible on all pages of the site allowing users to easily navigate the different features of the application.
* The Navbar is dynamically populated, meaning that an anonymous user will have access to a different set of navigation options than a logged in user will. This allows for the easy control of the user's movement throughout the website.

### **Intro Section**
* The Intro Section provides the users with the key information needed to understand the main purpose of the website.
* Key words within the Intro Section are highlighted, allowing the user to understand at a glance the main functions of the application.

### **Recipe Cards Section**
* The Recipe Cards Section displays the entire collection of recipes present on the site.
* Each individual recipe is represented by card, which displays the recipe's key information including its name, description, author and the dietary category of the recipe.
* The dietary category of the recipe is indicated with a small icon at the head of the card, which can currently represent the following categories: 'Meat Eater', 'Vegetarian' and 'Vegan'.
* Clicking on a recipe card takes the user to the view_recipe template associated with that recipe.

### **Footer**
* The website displays a basic footer at the end of every page.
* Originally dynamically populated by JavaScript HTML injection, the Footer's content is now hardcoded.

### **Authentication - Sign Up/Login**
* Authentication is handled using the Flask-Login package.
* Users can (and are encouraged to) Sign Up to the website by clicking on the highlighted 'Sign Up' navigation element.
* Upon clicking on the Sign Up navigation element the user is redirected to the Sign Up template, whereupon they will be prompted to enter a username and a password.
* The username and password are validated in the backend. Usernames must be unique, both fields must be of a certain length, and the password is hashed using Bcrypt.
* If the user submits the Sign Up form with a valid username and password, they are redirected to the Login template.
* The user is prompted to enter their Login credentials, and if they successfully do so they are redirected to the 'My Profile' template.
* If logged in, a user can click the Log Out button at any time to end their session, and return their status to that of an anonymous user.

### **Authentication - Login Required**
* Flask-Login provides the Login Required functionality.
* Certain templates and functions within the application are inaccessible to anonymous users. This, in conjunction with other measures, protects the content of the database and the application.

### **Authentication - Content Protection**
* Custom code has been implemented which prevents one logged in user from accessing the content of another user.
* This means that User 1 cannot edit or delete recipes created by User 2.

### **My Profile**
* Upon successful Login, the user is presented with their personal profile template.
* A message, displaying the user's username, welcomes the user, while a sub-heading informs the user of the purpose of the 'My Profile' page.
* If the user has created any recipes, they are displayed within the My Profile template in the same card format as the Index template.
* As with the Index display, clicking on a recipe card takes the user to the view_recipe template associated with that recipe.
* Two buttons are present under each of the user's recipes:
    * The Delete Recipe button allows a user to remove a recipe from the database. This function requires confirmation through the use of a modal, reducing the chances of an accidental deletion.
    * The Edit Recipe button allows the user to access the recipe's update_recipe template, where they can use a form to change any of the data that they have entered in associated with that recipe.

### **Add Recipe**
* By clicking on either the + button in the index or in their profile, a registered and logged in user can access the Add Recipe template.
* The + button is not visible to anonymous users, and the route is protected by the Login Required function.
* The Add Recipe template provides the user with a 2 sided form to complete. The contents of this form, when submitted make up a full recipe entry in the database.
* The fields of the form are validated, and all fields must be filled out before submission can occur.

### **View Recipe**
* By clicking on any recipe card, the user is taken to that recipe card's View Recipe template.
* The view Recipe template displays all of the data associated with its corresponding recipe.
* If the recipe was created by the logged in user viewing it, additional update and delete buttons are present within the left side display.

### **Update Recipe**
* By clicking on the Update Recipe icon present in the Profile template, the user can access the Update Recipe template which allows them to change the data of a recipe that they have created.
* The Update Recipe template is a carbon copy of the Add Recipe template, except in that it is automatically pre-filled with a recipe's existing data.

### **Delete Recipe**
* By clicking on a recipe's delete icons (either in the Profile template's recipe display or in the View Recipe template) the user is presented with a modal, asking them to confirm the deletion.
* If the user confirms the deletion within the modal, the data related to that recipe is removed from the database and the user is returned to their Profile template.


 ## **Upcoming Features**
---
### **Separate Instruction/Ingredient Tables**
* Having separate Instruction and Ingredient tables would allow users to enter each of their instructions step by step and each ingredient one by one.
* In their current implementation, the ingredients and instructions sections of the form are somewhat free-form, with their contents being displayed according to the way the user inputs the information.
* This new structure would allow for a homogenised recipe viewing experience
* In this format, additional page styling could present the list of instructions in ordered steps, perhaps with checkboxes for the user to tick as they work their way through the recipe.

### **Recipe Aggregation - Cookbooks**
* Allowing users to aggregate recipes into different collections or 'Cookbooks' would add value to the site.
* Users should simply be able to create a new Cookbook instance, and when viewing a recipe should be able to click a dropdown to add the recipe to any of their existing Cookbooks.

### **Recipe Searching**
* Users should be able to easily search for specific recipes.
* To achieve this, in all areas where a recipe display is present, the user should have access to a search input, which will filter the recipes displayed to match the user's search terms.

### **Additional Diet Categories**
* Currently, the site's recipes are broken into 3 basic dietary categories of 'Meat Eater', 'Vegetarian' and 'Vegan'.
* These categories do not account for the wide variety of dietary categories in the real world and should be expanded upon.

### **Responsivity**
* In its current form, the site is not functional across all screen sizes, having been designed on, and designed for, large desktop monitors.
* In future development, the intention is to update the site to be functional and pleasant to use across a wide variety of screen sizes and ratios.

 ## **Testing**
---
This project utilises Unit Testing, as provided by the PyTest library, to test the various functions of the application.

Once the database has been initialised by create.py, the tests can be run by entering the following command into the terminal:

```
python3 -m pytest --cov=application
```

**NB:** The tests as currently supplied will only function correctly in the development branch, as this branch has form validation disabled. If form validation is not disabled, the tests will not function correctly.

At the time of writing, running the above command will return the following:

![](README_Assets/Test-Report.png)

The tests check (almost, see below) the entire custom codebase in routes.py, ensuring that the site's functionality is performing as expected. All of the actions that a user can undertake are tested and none of the tests currently fail. The test suite has been designed with expansion in mind, allowing for the addition of extra tests to examine the results of edge case user inputs.

The functionality not tested is that which relies on Flask-Login. Such testing of an external framework is beyond the scope of this project, and while it would be nice to have 100% coverage, I have received advice from a QA training that such a thing would not be feasible in the time-frame available.


 ## **Known Issues**
---
### **Button Edges Unresponsive**
* Presently, some of the site's buttons do not register a click event if the user clicks on the very outward edge.
* Buttons affected: Add Recipe Button, Edit Recipe Button, Delete Recipe Button
* This unintended occurrence is repeatable, but not of a severity that would hamper the user's experience. In fact, it is unlikely that the user would identify the problem unless looking for it.
* This issue can be fixed by restructuring the layout of the affected button's HTML, and then updating the CSS to take the changes into account.
### **Lack of Responsivity**
* In its current form, the site is not functional across all screen sizes, having been designed on and for large desktop monitors.
* This issue can be fixed by adding media queries to the various site elements, resizing and removing elements to improve the small screen experience.
 ## **Data Structure**
---
### **Database Schema**
* Currently, the database comprises of two tables:
    * User
    * Recipe
* The User table holds the data about the site's registered users, including:
    * ID
    * Username
    * Password
* The Recipe table holds the data about all of the site's recipes, as created by users. This data includes:
    * ID
    * Name
    * Author
    * Description
    * Cooking_Time
    * Servings
    * Diet
    * Ingredients
    * Instructions

The following Entity Relationship Diagram describes the contents of the database, including future plans for additional tables.
![](README_Assets/Recipease_Entity_Relationship_Diagram.jpeg)


 ## **Site Structure**
---
### **Layout:**
* The site has been designed with simplicity of navigation at the forefront of concerns.
* The main Navigation Bar is present at the head of every page, allowing the user to easily identify and move between the different sections of the site.
* The Index template has been designed to inform a new user of the purpose of the site, with careful highlighting to draw the eye to different important information/buttons.

### **User Flow Map**
The following User Flow Map describes the layout of the site and the expected paths that a user may take.

<br>

 ![](README_Assets/Recipease_User_Flow_Chart.jpeg)

 ## **Design**
---
### Overview
The website has been designed to look sleek and modern, and includes the use of Neumorphic elements to give the site a tactile feel. Buttons and forms are designed to be inviting, and subtle animation effects engage the user and let them see the results of their actions.
Additional animation was present in early versions of the site, however these animations were sidelined at a certain point in development. Reimplementing these animations would not take significant time or energy, and so it is to be hoped that at some point in the future that they will make a return.

### Colours
Dark colours were used throughout the project, with the aim being to use two similar colours for structure, one for text and another for highlighting different important information.

The main colours used throughout the website can be viewed below:

![](README_Assets/Color_Palette.png)

### Design Documents
Following on from the wireframes created in the planning phase of the project, higher fidelity design documents were created to more accurately capture the feel of the site, and to provide a strong basis from which to implement the required HTML and CSS.

These design documents can be viewed below:

### Index
![](README_Assets/Designs/Index.png)

### Authentication
![](README_Assets/Designs/Authentication.png)

### Profile
![](README_Assets/Designs/Profile.png)

### Create/Update Recipe
![](README_Assets/Designs/Create_Update_Recipe.png)

### View Recipe
![](README_Assets/Designs/View_Recipe.png)

 ## **Technologies Used**
---
### **Flask**
* The Flask micro-framework has been used to create this application.
* Flask provides built-in templating, routing and WSGI.
* Flask can be extended using a variety of packages, which proved instrumental in the development of this application.

### **Flask-Login**
* Flask-Login provides the basis for the site's authentication functionalities.
* Pre-built Signup and Login functionality, as well as the hashing of passwords using Bcrypt, allows for the safe and hassle-free registration of new users to the site.
* Flask Login allows for the gating of content depending on a user's authentication status, a feature used to protect the database from unauthorised access.

### **SQLite**
* SQLite provides an in-memory database for use in a non-production environment. 
* In the event that this project was to be used in production environment, an alternative database solution would be required.

### **SQLAlchemy**
* SQLAlchemy is the library used that served as the Object Relational Mapping tool, which translate Python classes to tables within the database.

### **WTForms**
* WTForms is the library used to render the forms into which users input their data.
* This library features CSRF protection and data validation, both of which secure the contents of the database.

### **Github**
* The version control of this project is handled by GitHub.
* Using Github and its GUI makes performing Git actions more visual and straightforward, allowing easy identification of key information at a glance.

### **GitPod**
* GitPod was the IDE used during the development of this project.
* Essentially a cloud based version of VS Code, GitPod allows for great mobility and flexibility, being usable on almost any device.

### **Font Awesome**
* Font Awesome is used to provide the iconography of the site.
* Font Awesome's functionality is served via a CDN.

### **Trello**
* Trello was used throughout the project to keep track of the various tasks to be completed in the realisation of the work.

### **Figma**
* Figma was used to create high fidelity design mock-ups of the site's templates. 

### **Balsamiq**
* Balsamiq was used to create low fidelity wireframes of the site's templates. 

 ## **Acknowledgements**
---
### My sincere thanks to the following people and groups; I greatly appreciate the assistance and support that they provided during the development of this app.

<br>

* Adam Gray - QA Instructor
* Earl Gray - QA Instructor
* Leon Robinson - QA Instructor
* Jacqueline Adams - AMS Senior Recruiter
* Team Magenta - My Peers