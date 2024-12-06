# `pages` Folder

LISAA

Overview: 
    NU.Compass is a web application designed to enhance the global experience for all Northeastern University students, with a specific focus on first-year global study abroad participants. The app addresses key pain points faced by students preparing for or returning from study abroad programs, such as the lack of pre-departure mentorship, fragmented communication channels, and limited transparency around program experiences. By collecting, storing, and analyzing user data, NU.Compass builds a robust repository of location ratings, mentorship success stories, and popular FAQs, empowering incoming students to make informed decisions, connect with relevant mentors, and access tailored insights for their specific programs. 

    The application utilizes a containerized architecture with Docker, allowing for easy deployment and scalability. It interacts with a database, and all necessary SQL files will be executed on startup to initialize the database schema, ensuring the system is always ready to store and retrieve the data it needs to function effectively.

    NU.Compass serves four major user categories. 
        1. Study-abroad alumni, who wish to mentor or network with peers after completing their time abroad.
        2. Students going abroad, who need guidance and preparation before departure. 
        3. Northeastern global experience staff, who seek to engage and support students effectively.
        4. Northeastern IT staff, who are responsible for maintaining the app, ensuring it stays updated, and monitoring user behavior to ensure adherence to community guidelines.
        
    Key features of NU.Compass include an ratings system, mentorship matching, an interactive Q&A forum, and the ability to search study abroad programs for easier decision-making. Students will be able to see study abroad programs with ratings, comments, questions, and replies -- all posted or answered by other students themselves. These features combine to help students access personalized mentorship, share experiences, and make confident choices about their study abroad journey.

    Ultimately, NU.Compass is more than just an app—it's a transformative tool that promotes informed choices, fosters peer support, and creates lasting connections in the global study abroad experience. By improving communication and providing valuable resources, NU.Compass helps ensure that students are well-prepared and supported throughout their global academic endeavors.


Table of Contents: 
    1. Prequisites 
    2. Setup Instructions 
    3. Running the Application 
    4. Team Members 
    5. Additional Notes 

Prerequisites: 
    - Docker is required to build and run the containers. 
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
        Run the following command: docker compose up db -d 
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
    1. Docker Errors: 
        Ensure that Docker is running, so try running docker compose down db followed by docker compose up db -d
    2. Rebuilding Containers: 
        If  you make changes to the Dockerfile, rebuild the containers with: docker-compose up --build -d
    3. Page organization:
        Tim Waltz - references pages starting with '1'. Pages 10, 11, 12, 13 14
        Tom Holland - references pages 5, 11, 13, 33
        System Administrator - references page 5, 25, 28, 32
        Global Experience Staff - references page 5, 22, 24, 25, 33.
    4. Flask Blueprints Ordering 
        The ordering of the flask blueprints is by table. This means that each table corresponds to its own blueprint, so students, locations, abroad_programs, etc each have their own blueprint. By ordering the blueprint this way, it makes it easier to extend or modify parts of the application independently. 
    5. For CS3200 TAs and Prof Fontenot: The ER, Relational, and SQL Diagrams/Databases have been updated and improved since phase 2 of this project. 
        
Link to Project Demo: https://youtu.be/AC8zt0zVE2k