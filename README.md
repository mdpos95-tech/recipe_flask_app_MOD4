# recipe_flask_app_MOD4

--------------------------------------------------------------------------------------------------------------------

# The Kitchen Collective //-

# The Why?
I chose this project after speaking with my mother, who mentioned that she and her sisters often share recipes through text messages and phone calls. Overtime, many of those recipes became difficult to find as they were buried in long message threads.

This inspired me to create a website where users could register, share recipes, save favourites and organise recipes into categories, making them easy to find and revisit whenever needed.

The project provided an opportunity to fulfill the requirements of my Module 4 Database project while also creating something that could be genuinely useful for my family and other food enthusiasts.

# Project overview
- The Kitchen Collective is a recipe sharing web application developed as part of my Database module. The aim of the project was to design and build a database driven website that allows users to register accounts, create recipes, browse recipescreated by other users, save favourites, and interact through comments.

- This project gave me practical experience working with relational databases, CRUD operations, user authentication, form validation, and full-stack web development using Python and Flask.


# Technologies Used
- Python
- Flask
- SQLAlchemy
- PostgresSQL
- HTML5
- CSS3
- JavaScript
- WTForms
- Flask-Login
- Render (for deployment)
- Git & GitHub


# Features //-

# User Authentication
- User can:
   Register a new account.
   Log in securely.
   Log out.
   Access protected areas of the website.
 // Passwords are securely hashed before being stored in the database.


 # Recipe Management (CRUD)
- Authenticated users can:
  Create recipes.
  View recipes.
  Update their own recipes.
  Delete their own recipes.
 // This feature demonstrates the implementation of CRUD operations.


# Categories
- Recipes are organised into categories such as Breakfast, Lunch, Dinner, and Dessert. Categories are stored in a seperate database table and linked to recipes through relationships.


# Search and Filtering
- Users can search recipes by title and filter recipes by category.


# Favourites
- Users can save recipes to a favourites list for quick access later.


# Comments 
- Users can leave comments on recipes, allowing interaction between members of the community.


# Responsive Design
- The website has been designed to work on desktop, tablet and mobile devices using CSS media queries.


# Database Design //-

The application uses a relational database consisting of multiple related tables.

Main entities include:

- Users
- Recipes
- Categories
- Comments
- Favourites

Relationships were implemented using SQLAlchemy to demonstrate one-to-many and many-to-many database relationships.


# What I Learned //-

This project helped me gain practical experience applying databse concepts to a real-world application.

Some of the key concepts I learned inluced:

- Designing relational database structures.
- Creating and managing database relationships.
- Implementing CRUD functionality.
- Using SQLAlchemy ORM.
- User authentication and session management.
- Form validation using WTForms.
- Responsive web design.
- Deploying a Flask application.
- Version control using Git and GitHub.

One of the most valuable aspects of the project was seeing how database theory can be applied within a working web application. Building features such as favourites, comments and recipe management helped me better understand how relationships between tables are used in practice.


# Author //-

Mark O'Shea | Module 4 Database Project | 2026





