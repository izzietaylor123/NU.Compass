# `pages` Folder

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
        DB_HOST = localhost 
        DB_USER = root 
        DB_PASSWORD = 
        DB_NAME 

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

