
LISAA

Overview: 
    NU.Connect is a web application designed to enhance the global experience for all Northeastern University students, with a specific focus on first-year global study abroad participants. The app addresses key pain points faced by students preparing for or returning from study abroad programs, such as the lack of pre-departure mentorship, fragmented communication channels, and limited transparency around program experiences. By collecting, storing, and analyzing user data, NU.Connect builds a robust repository of location ratings, mentorship success stories, and popular FAQs, empowering incoming students to make informed decisions, connect with relevant mentors, and access tailored insights for their specific programs.

    The application utilizes a containerized architecture with Docker, allowing for easy deployment and scalability. It interacts with a database, and all necessary SQL files will be executed on startup to initialize the database schema, ensuring the system is always ready to store and retrieve the data it needs to function effectively.

    NU.Connect serves four major user categories: students going abroad, who need guidance and preparation before departure; study-abroad alumni, who wish to mentor or network with peers after completing their time abroad; Northeastern global experience staff, who seek to engage and support students effectively; and Northeastern IT staff, who are responsible for maintaining the app, ensuring it stays updated, and monitoring user behavior to ensure adherence to community guidelines. Key features of NU.Connect include an experience ratings system, mentorship matching, and an interactive Q&A forum. These features combine to help students access personalized mentorship, share experiences, and make confident choices about their study abroad journey.

    Ultimately, NU.Connect is more than just an app—it's a transformative tool that promotes informed choices, fosters peer support, and creates lasting connections in the global study abroad experience. By improving communication and providing valuable resources, NU.Connect helps ensure that students are well-prepared and supported throughout their global academic endeavors.


Table of Contents: 
    1. Prequisites 
    2. Setup Instructions 
    3. Running the Application 
    4. Flask Blueprints Ordering 
    5. Team Members 
    6. Controlling the Containers 
     

Prerequisites: 
    - Docker is required to build and run the containers. 
    - Docker Compose is needed to manage multi-container Docker. 
    - A GitHub Account
    - VSCode with the Python Plugin

Set up instructions: 
    1. Clone the repository
        git clone https://github.com/izzietaylor123/SQL_for_LISAA
    2. Install Docker and Docker Compose 
    3. Create .env file (need to  add password stuff) 
        DB_HOST = db 
        DB_USER = root 
        DB_PASSWORD = 'your_password_here'
        DB_NAME = lisaa_sql
    4. Install Python dependencies 
        In order to work on the backend code outside of docker do: 
        pip install -r requirements.txt

Running the application 
    1. Build and run the containers. 
        Run the following command: docker- compose up -d 
    2. Verify containers are running 
        docker ps 
    3. Access the Application 
        Once containers are running, the application should be accessiblee via http://localhost:8501 or the port defined in your .env file

Flask Blueprints Ordering 
    - The ordering of the flask blueprints is by table. This means that each table corresponds to its own blueprint, so students, locations, abroad_programs, etc each have their own blueprint.  

Team Members
    - Sarah Wang 
    - Ava Toren 
    - Lara Goyal 
    - Ashna Shah 
    - Isabel Taylor 

Controlling the Containers
    - `docker compose up -d` to start all the containers in the background
    - `docker compose down` to shutdown and delete the containers
    - `docker compose up db -d` only start the database container (replace db with the other services as needed)
    - `docker compose stop` to "turn off" the containers but not delete them. 


