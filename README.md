# Fall 2024 CS 3200 Project Template Repository

This repo is a template for your semester project.  It includes most of the infrastructure setup (containers) and sample code and data throughout.  Explore it fully and ask questions.

## Prerequisites

- A GitHub Account
- A terminal-based or GUI git client
- VSCode with the Python Plugin
- A distrobution of Python running on your laptop (Choco (for Windows), brew (for Macs), miniconda, Anaconda, etc). 

## Current Project Components

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for your data model and data base in the `./database-files` directory

## Suggestion for Learning the Project Code Base

If you are not familiar with web app development, this code base might be confusing. You will probably want two versions though:
1. One version for you to explore, try things, break things, etc. We'll call this your **Personal Repo** 
1. One version of the repo that your team will share.  We'll call this the **Team Repo**. 


### Setting Up Your Personal Repo

1. In GitHub, click the **fork** button in the upper right corner of the repo screen. 
1. When prompted, give the new repo a unique name, perhaps including your last name and the word 'personal'. 
1. Once the fork has been created, clone YOUR forked version of the repo to your computer. 
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
1. Start the docker containers. 

### Setting Up Your Team Repo 

Before you start: As a team, one person needs to assume the role of *Team Project Repo Owner*. 

1. The Team Project Repo Owner needs to fork this template repo into their own GitHub account **and give the repo a name consistent with your project's name**.  If you're worried that the repo is public, don't.  Every team is doing a different project. 
1. In the newly forked team repo, the Team Project Repo Owner should go to the **Settings** tab, choose **Collaborators and Teams** on the left-side panel. Add each of your team members to the repository with Write access. 
1. Each of the other team members will receive an invitation to join.  Obviously accept the invite. 
1. Once that process is complete, each team member, including the repo owner, should clone the Team's Repo to their local machines (in a different location than your Personal Project Repo).  

## Controlling the Containers

- `docker compose up -d` to start all the containers in the background
- `docker compose down` to shutdown and delete the containers
- `docker compose up db -d` only start the database container (replace db with the other services as needed)
- `docker compose stop` to "turn off" the containers but not delete them. 


## Handling User Role Access and Control

In most applications, when a user logs in, they assume a particular role.  For instance, when one logs in to a stock price prediction app, they may be a single investor, a portfolio manager, or a corporate executive (of a publicly traded company).  Each of those *roles* will likely present some similar features as well as some different features when compared to the other roles. So, how do you accomplish this in Streamlit?  This is sometimes called Role-based Access Control, or **RBAC** for short. 

The code in this project demonstrates how to implement a simple RBAC system in Streamlit but without actually using user authentication (usernames and passwords).  The Streamlit pages from the original template repo are split up among 3 roles - Political Strategist, USAID Worker, and a System Administrator role (this is used for any sort of system tasks such as re-training ML model, etc.). It also demonstrates how to deploy an ML model. 

Wrapping your head around this will take a little time and exploration of this code base.  Some highlights are below. 

### Getting Started with the RBAC 
1. We need to turn off the standard panel of links on the left side of the Streamlit app. This is done through the `app/src/.streamlit/config.toml` file.  So check that out. We are turning it off so we can control directly what links are shown. 
1. Then I created a new python module in `app/src/modules/nav.py`.  When you look at the file, you will se that there are functions for basically each page of the application. The `st.sidebar.page_link(...)` adds a single link to the sidebar. We have a separate function for each page so that we can organize the links/pages by role. 
1. Next, check out the `app/src/Home.py` file. Notice that there are 3 buttons added to the page and when one is clicked, it redirects via `st.switch_page(...)` to that Roles Home page in `app/src/pages`.  But before the redirect, I set a few different variables in the Streamlit `session_state` object to track role, first name of the user, and that the user is now authenticated.  
1. Notice near the top of `app/src/Home.py` and all other pages, there is a call to `SideBarLinks(...)` from the `app/src/nav.py` module.  This is the function that will use the role set in `session_state` to determine what links to show the user in the sidebar. 
1. The pages are organized by Role.  Pages that start with a `0` are related to the *Political Strategist* role.  Pages that start with a `1` are related to the *USAID worker* role.  And, pages that start with a `2` are related to The *System Administrator* role. 


## Deploying An ML Model (Totally Optional for CS3200 Project)

*Note*: This project only contains the infrastructure for a hypothetical ML model. 

1. Build, train, and test your ML model in a Jupyter Notebook. 
1. Once you're happy with the model's performance, convert your Jupyter Notebook code for the ML model to a pure python script.  You can include the `training` and `testing` functionality as well as the `prediction` functionality.  You may or may not need to include data cleaning, though. 
1. Check out the  `api/backend/ml_models` module.  In this folder, I've put a sample (read *fake*) ML model in `model01.py`.  The `predict` function will be called by the Flask REST API to perform '*real-time*' prediction based on model parameter values that are stored in the database.  **Important**: you would never want to hard code the model parameter weights directly in the prediction function.  tl;dr - take some time to look over the code in `model01.py`.  
1. The prediction route for the REST API is in `api/backend/customers/customer_routes.py`. Basically, it accepts two URL parameters and passes them to the `prediction` function in the `ml_models` module. The `prediction` route/function packages up the value(s) it receives from the model's `predict` function and send its back to Streamlit as JSON. 
1. Back in streamlit, check out `app/src/pages/11_Prediction.py`.  Here, I create two numeric input fields.  When the button is pressed, it makes a request to the REST API URL `/c/prediction/.../...` function and passes the values from the two inputs as URL parameters.  It gets back the results from the route and displays them. Nothing fancy here. 

 


This folder contains all the pages that will be part of the application. Details on required numbers will be provided in the Phase 3 documentation.

These pages are meant to show you an example of some of the features of Streamlit and the way we will limit functionality access by role/persona. It is not meant to represent a complete application.

TODO: Describe the pages folder and include link to documentation. Don't forget about ordering of pages.

LISAA

Overview: 
    NU.Connect is a web application designed to enhance the global experience for all Northeastern University students, with a specific focus on first-year global study abroad participants. The app addresses key pain points faced by students preparing for or returning from study abroad programs, such as the lack of pre-departure mentorship, fragmented communication channels, and limited transparency around program experiences. By collecting, storing, and analyzing user data, NU.Connect builds a robust repository of location ratings, mentorship success stories, and popular FAQs, empowering incoming students to make informed decisions, connect with relevant mentors, and access tailored insights for their specific programs.

    The application utilizes a containerized architecture with Docker, allowing for easy deployment and scalability. It interacts with a database, and all necessary SQL files will be executed on startup to initialize the database schema, ensuring the system is always ready to store and retrieve the data it needs to function effectively.

    NU.Connect serves four major user categories: students going abroad, who need guidance and preparation before departure; study-abroad alumni, who wish to mentor or network with peers after completing their time abroad; Northeastern global experience staff, who seek to engage and support students effectively; and Northeastern IT staff, who are responsible for maintaining the app, ensuring it stays updated, and monitoring user behavior to ensure adherence to community guidelines. Key features of NU.Connect include an experience ratings system, mentorship matching, an interactive Q&A forum, and the ability to favorite study abroad locations for easier decision-making. These features combine to help students access personalized mentorship, share experiences, and make confident choices about their study abroad journey.

    Ultimately, NU.Connect is more than just an app—it's a transformative tool that promotes informed choices, fosters peer support, and creates lasting connections in the global study abroad experience. By improving communication and providing valuable resources, NU.Connect helps ensure that students are well-prepared and supported throughout their global academic endeavors.


Table of Contents: 
    1. Prequisites 
    2. Setup Instructions 
    3. Running the Application 
    4. Team Members 
    5. Additional Notes 

Prerequisites: 
    - Docker is  required to build and run the containers. 
    - Docker Compose is needed to manage multi-container Docker. 
    - Git must be installed to clone the repository. 

Set up instructions: 
    1. Clone the repository
        git clone https://github.com/izzietaylor123/SQL_for_LISAA
    2. Create .env file (need to  add password stuff) 
        DB_HOST = db 
        DB_USER = root 
        DB_PASSWORD = 
        DB_NAME = lisaa_sql

Running the application 
    1. Build and run the containers. 
        Run the following command: docker- compose up -d 
    2. Verify containers are running 
        docker ps 
    3. Access the Application 
        Once containers are running, the application should be accessibleee via http://localhost:8501 or the port defined in your .env file

Team Members
    - Sarah Wang 
    - Ava Toren 
    - Lara Goyal 
    - Ashna Shah 
    - Isabel Taylor 

Additional Notes 
    1. Docker  Errors: 
        Ensure that Docker is running, so try running docker-compose down followed by docker- compose up -d
    2.Rebuilding Containers: 
        If  you make changes to the Dockerfile, rebuild the containers with: docker-compose up --build -d

