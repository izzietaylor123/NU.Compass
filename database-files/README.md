# `database-files` Folder

TODO: Put some notes here about how this works.  include how to re-bootstrap the db. 

The SQL_for_LISAA.sql file contains all of our table create and data insertion functions into our main database for this project. This database contains a comprehensive set of information on abroad programs, locations, students, employees, courses, majors, questions, replies, and ratings in order to provide an overview for different abroad programs hosted by Northeastern University. 

In order to re-bootstrap the db, access the VS code terminal and type
"docker compose down", 
followed by docker compose up -d" 
in order to reset all db changes made in the front end and access the most recent updated db. 

Changes can be made to the db and are shown on the Streamlit page and in DataGrip if this db is loaded into DataGrip and manipulation occurrs on the front end. Updates to the manual inserts will not be shown within the .sql file. Make sure to create a datasource with the following specifications:

- username = root
- password = <env_password_here>
- port = 3200 (as specified in docker compose)
