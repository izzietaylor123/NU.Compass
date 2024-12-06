Overview: NU.Compass is a web application designed to enhance the global experience for all Northeastern University students, with a specific focus on first-year global study abroad participants. The app addresses key pain points faced by students preparing for or returning from study abroad programs, such as the lack of pre-departure mentorship, fragmented communication channels, and limited transparency around program experiences. By collecting, storing, and analyzing user data, NU.Compass builds a robust repository of location ratings, mentorship success stories, and popular FAQs, empowering incoming students to make informed decisions, connect with relevant mentors, and access tailored insights for their specific programs.

The application utilizes a containerized architecture with Docker, allowing for easy deployment and scalability. It interacts with a database, and all necessary SQL files will be executed on startup to initialize the database schema, ensuring the system is always ready to store and retrieve the data it needs to function effectively.

NU.Compass serves four major user categories: students going abroad, who need guidance and preparation before departure; study-abroad alumni, who wish to mentor or network with peers after completing their time abroad; Northeastern global experience staff, who seek to engage and support students effectively; and Northeastern IT staff, who are responsible for maintaining the app, ensuring it stays updated, and monitoring user behavior to ensure adherence to community guidelines. Key features of NU.Compass include an experience ratings system, mentorship matching, and an interactive Q&A forum. These features combine to help students access personalized mentorship, share experiences, and make confident choices about their study abroad journey.

Ultimately, NU.Compass is more than just an app—it's a transformative tool that promotes informed choices, fosters peer support, and creates lasting connections in the global study abroad experience. By improving communication and providing valuable resources, NU.Compass helps ensure that students are well-prepared and supported throughout their global academic endeavors.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
3. [Running the Application](#running-the-application)
4. [Using a Python Virtual Environment](#using-a-python-virtual-environment)
5. [Flask Blueprints Ordering](#flask-blueprints-ordering)
6. [Team Members](#team-members)
7. [Controlling the Containers](#controlling-the-containers)

---

## Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) for containerization.
- A GitHub account.
- [VSCode](https://code.visualstudio.com/) with the Python plugin installed.

---

## Setup Instructions
1. **Clone the Repository**:
   ```
   git clone https://github.com/izzietaylor123/SQL_for_LISAA
   cd SQL_for_LISAA
   ```

2. **Install Docker and Docker Compose**:
   Ensure Docker is installed and running on your system.

3. **Create a `.env` File**:
   Create a `.env` file in the root directory with the following content:
   ```
   DB_HOST=db
   DB_USER=root
   DB_PASSWORD=your_password_here
   DB_NAME=lisaa_sql
   ```

4. **Install Python Dependencies**:
   To work on the backend code outside of Docker:
   ```
   pip install -r requirements.txt
   ```

---

## Running the Application
1. **Build and Run the Containers**:
   ```
   docker-compose up -d
   ```

2. **Verify Running Containers**:
   ```
   docker ps
   ```

3. **Access the Application**:
   The application should be accessible at [http://localhost:8501](http://localhost:8501) or the port specified in your `.env` file.

---

## Using a Python Virtual Environment
1. **Create and Activate a Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   With the virtual environment activated, you can run the application locally using the usual Python commands.
   ```
   flask run
   ```

---

## Flask Blueprints Ordering
The ordering of the flask blueprints is by table. This means that each table corresponds to its own blueprint, so students, locations, abroad_programs, etc., each have their own blueprint. By ordering the blueprint this way, it makes it easier to extend or modify parts of the application independently.

---

## Team Members
- Sarah Wang
- Ava Toren
- Lara Goyal
- Ashna Shah
- Isabel Taylor 

---

## Controlling the Containers
- ``` docker compose up -d ``` to start all the containers in the background
- ``` docker compose down ``` to shutdown and delete the containers
- ``` docker compose up db -d ``` to only start the database container (replace db with the other services as needed)
- ``` docker compose stop ``` to "turn off" the containers but not delete them.