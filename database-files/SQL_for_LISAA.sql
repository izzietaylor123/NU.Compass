SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0;
SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'TRADITIONAL,ALLOW_INVALID_DATES';

DROP DATABASE IF EXISTS `lisaa_sql`;
CREATE DATABASE `lisaa_sql` DEFAULT CHARACTER SET latin1;
USE `lisaa_sql`;

DROP DATABASE IF EXISTS `lisaa_sql`;
CREATE DATABASE `lisaa_sql` DEFAULT CHARACTER SET latin1;
USE `lisaa_sql`;

DROP TABLE IF EXISTS Location;
CREATE TABLE IF NOT EXISTS Location
(
    locationID  INT(11)     NOT NULL AUTO_INCREMENT,
    city        VARCHAR(50) NOT NULL,
    country     VARCHAR(50) NOT NULL,
    description LONGTEXT    NOT NULL,
    PRIMARY KEY (locationID)
);

DROP TABLE IF EXISTS abroadProgram;
CREATE TABLE IF NOT EXISTS abroadProgram
(
    programID       INT(11) PRIMARY KEY,
    programName     VARCHAR(100)   NOT NULL,
    prgmDescription LONGTEXT       NOT Null,
    locationID      INT(11) UNIQUE NOT NULL,
    programType     VARCHAR(100)   NOT NULL,
    empID           INT(11) UNIQUE NOT NULL
    CONSTRAINT location_fk FOREIGN KEY (locationID)
        REFERENCES Location (locationID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS Rating;
CREATE TABLE IF NOT EXISTS Rating
(
    ratingID   INT(11)  NOT NULL AUTO_INCREMENT,
    programID  INT(11)  NOT NULL,
    sID        INT(11)  NOT NULL,
    datePosted DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    locRating  INT(11)  NOT NULL,
    profRating INT(11)  NOT NULL,
    atmosphereRating  INT(11)  NOT NULL,
    comment    LONGTEXT NOT NULL,
    PRIMARY KEY (ratingID),
    CONSTRAINT rating_fk_01 FOREIGN KEY (programID)
        REFERENCES abroadProgram (programID)
    CONSTRAINT student_rating FOREIGN KEY (sID)
        REFERENCES Student (sID)
);


DROP TABLE IF EXISTS Alerts;
CREATE TABLE IF NOT EXISTS Alerts
(
    alertID    INT(11) NOT NULL AUTO_INCREMENT,
    locationID INT(11) NOT NULL,
    message    VARCHAR(200),
    datePosted DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (alertID),
    CONSTRAINT alerts_fk_01 FOREIGN KEY (locationID)
        REFERENCES abroadProgram (locationID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS Resources;
CREATE TABLE IF NOT EXISTS Resources
(
    resourceID  INT(11)  NOT NULL AUTO_INCREMENT,
    locationID  INT(11)  NOT NULL,
    category    VARCHAR(100),
    lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (resourceID),
    CONSTRAINT resources_fk_01 FOREIGN KEY (locationID)
        REFERENCES abroadProgram (locationID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS Course;
CREATE TABLE IF NOT EXISTS Course
(
    courseID          INT(11)        NOT NULL AUTO_INCREMENT,
    courseName        VARCHAR(200)   NOT NULL,
    courseDescription LONGTEXT       NULL DEFAULT NULL,
    programID         INT(11)        NOT NULL,
    professorID       INT(11) UNIQUE NOT NULL,
    PRIMARY KEY (courseID),
    CONSTRAINT course_fk_01 FOREIGN KEY (programID)
        REFERENCES abroadProgram (programID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS adminEmployee;
CREATE TABLE IF NOT EXISTS adminEmployee
(
    empID    INT(11) PRIMARY KEY,
    title    VARCHAR(100)   NOT NULL,
    fName    VARCHAR(50)    NOT NULL,
    lName    VARCHAR(50)    NOT NULL,
    email    VARCHAR(50)    NOT NULL,
    courseID INT(11) UNIQUE NOT NULL,
    UNIQUE(empID)
    CONSTRAINT course_fk_02 FOREIGN KEY (courseID)
        REFERENCES Course (courseID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS employeeAbroadProgram;
CREATE TABLE IF NOT EXISTS employeeAbroadProgram
(
    programID INT(11) NOT NULL,
    empID     INT(11) NOT NULL,
    PRIMARY KEY (programID, empID),
    CONSTRAINT eap_pk_00 FOREIGN KEY (programID)
        REFERENCES abroadProgram (programID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT eap_pk_01 FOREIGN KEY (empID)
        REFERENCES adminEmployee (empID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS engagementAnalytics;
CREATE TABLE IF NOT EXISTS engagementAnalytics
(
    featureID  INT(11) PRIMARY KEY,
    empID      INT(11)  NOT NULL,
    usageCount INT      NOT NULL,
    date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT eng_analytics_fk_01 FOREIGN KEY (empID)
        REFERENCES adminEmployee (empID)
);




DROP TABLE IF EXISTS Professor;
CREATE TABLE IF NOT EXISTS Professor
(
    profID     INT(11)      NOT NULL AUTO_INCREMENT,
    fName      VARCHAR(200) NOT NULL,
    lName      VARCHAR(200) NOT NULL,
    department VARCHAR(200),
    email      VARCHAR(200),
    PRIMARY KEY (profID),
    CONSTRAINT professor_fk_01 FOREIGN KEY (profID)
        REFERENCES Course (professorID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Student;
CREATE TABLE IF NOT EXISTS Student
(
    sID       INT(11)      NOT NULL AUTO_INCREMENT,
    fName     VARCHAR(20)  NOT NULL,
    lName     VARCHAR(20)  NOT NULL,
    email     VARCHAR(200) NOT NULL,
    blurb     VARCHAR(2000),
    role      VARCHAR(100) NOT NULL,
    INDEX idx_last_name (lName),
    PRIMARY KEY (sID)
);

DROP TABLE IF EXISTS studentAbroadProgram;
CREATE TABLE IF NOT EXISTS studentAbroadProgram
(
    programID INT(11) NOT NULL,
    sID       INT(11) NOT NULL,
    PRIMARY KEY (programID, sID),
    CONSTRAINT sap_pk_00 FOREIGN KEY (programID)
        REFERENCES abroadProgram (programID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT sap_pk_01 FOREIGN KEY (sID)
        REFERENCES Student (sID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


DROP TABLE IF EXISTS mentorshipMatch;
CREATE TABLE IF NOT EXISTS mentorshipMatch
(
    matchID     INT(11) NOT NULL AUTO_INCREMENT,
    menteeID    INT(11) NOT NULL,
    mentorID    INT(11) NOT NULL,
    dateMatched DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_match_id (matchID),
    PRIMARY KEY (matchID),
    CONSTRAINT mentorship_match_fk_01 FOREIGN KEY (mentorID)
        REFERENCES Student (sID),
    CONSTRAINT mentorship_match_fk_02 FOREIGN KEY (menteeID)
        REFERENCES Student (sID)
);


DROP TABLE IF EXISTS Major;
CREATE TABLE IF NOT EXISTS Major
(
    majorID    INT(11)      NOT NULL,
    majorName  VARCHAR(200) NOT NULL,
    Department VARCHAR(200),
    INDEX idx_major_name (majorName),
    PRIMARY KEY (majorID)
);

DROP TABLE IF EXISTS studentMajor;
CREATE TABLE IF NOT EXISTS studentMajor
(
    majorID INT(11) NOT NULL,
    sID     INT(11) NOT NULL,
    PRIMARY KEY (majorID, sID),
    CONSTRAINT sm_pk_00 FOREIGN KEY (majorID)
        REFERENCES Major (majorID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT sm_pk_01 FOREIGN KEY (sID)
        REFERENCES Student (sID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS Question;
CREATE TABLE IF NOT EXISTS Question
(
    qID        INT(11) NOT NULL AUTO_INCREMENT,
    sID        INT(11) NOT NULL,
    content    VARCHAR(2000),
    datePosted DATETIME DEFAULT CURRENT_TIMESTAMP,
    isApproved BOOLEAN,
    abroadProgram INT(11),
    PRIMARY KEY (qID),
    CONSTRAINT question_fk_01 FOREIGN KEY (sID)
        REFERENCES Student (sID),
    CONSTRAINT question_program_fk FOREIGN KEY (abroadProgram)
        REFERENCES abroadProgram (programID)
);

DROP TABLE IF EXISTS Reply;
CREATE TABLE IF NOT EXISTS Reply
(
    replyID    INT(11) PRIMARY KEY,
    sID        INT(11) NOT NULL,
    qID        INT(11) NOT NULL,
    content    VARCHAR(2000),
    datePosted DATETIME DEFAULT CURRENT_TIMESTAMP,
    isApproved BOOLEAN,
    CONSTRAINT reply_fk_01 FOREIGN KEY (sID)
        REFERENCES Student (sID)
        ON DELETE NO ACTION
        ON UPDATE CASCADE,
    CONSTRAINT reply_fk_02 FOREIGN KEY (qID)
        REFERENCES Question (qID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


## Making the data entries
INSERT INTO abroadProgram(programID, programName, prgmDescription, locationID, programType, empID)
VALUES ( 00000000001, 'NUin.ROME', 'Embark on a transformative academic journey in the heart of Rome, Italy—a city where history, art, philosophy, and culture converge. The NUIN Rome program offers a curated selection of humanities courses designed to immerse students in the richness of Western civilization while fostering a deep appreciation for global perspectives.
Through an interdisciplinary approach, students explore the historical, cultural, and philosophical dimensions of Rome as a living classroom. Courses are taught by distinguished faculty and emphasize critical thinking, analytical writing, and intercultural understanding. Students have the opportunity to engage directly with the city''s iconic landmarks, from the Colosseum to the Vatican, as part of their coursework, connecting theory to real-world experience.'
       , 00000000001, 'NU.in', 00000000001),
       ( 00000000002, 'Dialogue in London', 'Immerse yourself in the vibrant history and cutting-edge innovations of London, one of the world’s leading hubs for science, technology, and culture. This Dialogue of Civilizations program is designed for College of Science majors eager to explore the intersections of scientific discovery, societal impact, and cultural development.
Students will delve into the history of science in the UK, from the groundbreaking contributions of figures like Newton and Darwin to modern advancements in fields such as medicine, environmental science, and artificial intelligence. Through interactive coursework, guest lectures from leading scientists, and visits to renowned institutions such as the Natural History Museum, the Science Museum, and the Francis Crick Institute, participants will gain a holistic understanding of how science shapes—and is shaped by—society.'
       , 00000000002, 'Dialogue of Civilizations ', 00000000002);

INSERT INTO Alerts (alertID, locationID, message)
VALUES (00000000001, 00000000001, 'WARNING: High tempertures today. Keep hydrated and avoid the sun.'),
       (00000000002, 00000000002, 'Classes are cancelled for the day due to poor weather.');

INSERT INTO Resources (resourceID, locationID, category)
VALUES (00000000001, 00000000001, 'Academics'),
       (00000000002, 00000000002, 'Food & Restaurants');

INSERT INTO Student(sID, fName, lName, email, majorID, blurb, role, programID)
VALUES (00000000101, 'Kristen', 'Bell', 'kristen.bell@gmail.com', 00000000002, 'Loves exploring new cities', 'mentee',
        00000000001),
       (00000000102, 'Jackie', 'Torres', 'jtorres@gmail.com', 00000000001, 'Passionate about international relations',
        'mentee', 00000000002),
       (00000000201, 'Leighton', 'Meester', 'leighmeester@gmail.com', 00000000002, 'Interested in behavioral economics',
        'mentor', 00000000002),
       (00000000202, 'Ed', 'Westwick', 'e.west@gmail.com', 00000000001, 'All things politics', 'mentor', 00000000002);

INSERT INTO mentorshipMatch (matchID, menteeID, mentorID)
VALUES (00000000001, 00000000101, 00000000201),
       (00000000002, 00000000102, 00000000202);

INSERT INTO Major (majorID, majorName, department)
VALUES (00000000001, 'International Relations', 'Political Science'),
       (00000000002, 'Economics', 'Humanities');

INSERT INTO Location(locationID, city, country, description)
VALUES (00000000001, 'Rome', 'Italy',
        'Discover the heart of Western civilization in Rome, where ancient history, art, and culture come alive. Explore iconic landmarks like the Colosseum and Vatican City while delving into humanities courses that connect the city''s rich past to contemporary global issues.'),
       (00000000002, 'London', 'United Kingdom',
        'Immerse yourself in London, a global epicenter of science, technology, and culture. From the halls of the British Museum to cutting-edge research institutions, this program bridges the history of scientific discovery with its modern-day impact on society.');

INSERT INTO Rating(programID, sID, locRating, profRating, avgRating, comment)
VALUES (00000000001, 00000000001, 5, 4.5, 4.7,
        'This was a fun program! Would have liked to see more professor and course in the historical environment.'),
       (00000000002, 00000000002, 4, 4.5, 4.25,
        'Dialogue in London was great! I loved seeing the clock tower and Princess Diana. Classes were very engaging, but weather was dreary.');

INSERT INTO adminEmployee(empID, title, fName, lName, email, courseID)
VALUES (00000000001, 'IT Administrator', 'Timothee', 'Chalamet', 'timmychal@gmail.com', 00000000001),
       (00000000002, 'Global Advice Personnel', 'James', 'Bond', 'bond.james@gmail.com', 00000000002);

INSERT INTO engagementAnalytics(featureID, empID, usageCount)
VALUES (00000000001, 00000000002, 3),
       (00000000002, 00000000001, 8);

INSERT INTO Course(courseID, courseName, courseDescription, programID, professorID)
VALUES (00000000001, 'Introduction to Databases',
        'Data is everywhere!  This course will introduce you to relational database management systems (RDBMS).  We will study the foundations of the relational model, design of a relational database, SQL, use of a modern RDBMS, and more advanced topics as time permits. Prerequisites for this course are CS2500 or DS 2000 or EECE 2560.',
        00000000001, 00000000001),
       (00000000002, 'Intro to London Architecture',
        'This course introduces students to the history of Britain and its interaction with the world. The course follows British history from the Roman Empire to the present-day. The aim is to examine Britain’s relationships with other countries and cultures, exploring social, economic, and cultural developments, as well as political and diplomatic ones. As well as understanding these developments discretely, students will also be encouraged to see how they affect one another.',
        00000000002, 00000000002);

INSERT INTO Professor(profID, fName, lName, department, email)
VALUES (00000000001, 'Mark', 'Fontenot', 'Computer Science', 'fontenot.m@northeastern.edu'),
       (00000000002, 'Harry', 'Potter', 'History', 'potter.h@hogwarts.edu');

INSERT INTO Reply(replyID, sID, qID, content, datePosted, isApproved)
VALUES (00000000001, 00000000001, 00000000001,
        'The food was so delicious and the people were so kind. Definitely get a good pair of sneakers because you will be doing a lot of walking.',
        DEFAULT, 1),
       (00000000002, 00000000002, 00000000002, 'The professor was such an idiot!!', DEFAULT, 0);

INSERT INTO Question(qID, sID, content, datePosted, isApproved)
VALUES (00000000001, 00000000001, 'What is Rome like?', DEFAULT, 1),
       (00000000002, 00000000002, 'Poopoo Peepee!!!', DEFAULT, 0);

INSERT INTO studentAbroadProgram (programID, sID)
VALUES (00000000001, 00000000001),
       (00000000002, 00000000002);

INSERT INTO employeeAbroadProgram (programID, empID)
VALUES (00000000001, 00000000001),
       (00000000002, 00000000002);

INSERT INTO studentMajor (majorID, sID)
VALUES (00000000001, 00000000001),
       (00000000002, 00000000002);

--------------- PERSONA 1
---------------

-- 1.1: Creating a reply
INSERT INTO Reply (replyID, sID, qID, isApproved)
VALUES (00000000003, 00000000456, 00000000123, FALSE);

-- 1.2: Creating ratings
INSERT INTO Rating (ratingID, programID, sID, locRating, profRating, avgRating, comment)
VALUES (DEFAULT, 00000000001, 00000000456, 5, 4, 4.5, 'Great program and location!');

-- 1.3: Reading/selecting the location that the student studied abroad at
SELECT sap.programID, ap.programName, ap.prgmDescription, loc.city, loc.country
FROM studentAbroadProgram sap
         JOIN abroadProgram ap
              ON sap.programID = ap.programID
         JOIN Location loc
              ON ap.locationID = loc.locationID
WHERE sap.sID = 00000000456;

-- 1.4: Updating the blurb
UPDATE Student
SET blurb = 'I’ve added more experience since my time in Rome!'
WHERE sID = 00000000456;

-- 1.5: Reading/filtering potential mentees by specific majors
SELECT s.sID, s.fName, s.lName, m.majorName, sap.programID
FROM Student s
         JOIN studentMajor sm
              ON s.sID = sm.sID
         JOIN Major m
              ON sm.majorID = m.majorID
         JOIN studentAbroadProgram sap
              ON s.sID = sap.sID
WHERE m.majorName = 'Business'
  AND sap.programID = 00000000001;

-- 1.6: Creating and Deleting mentorship match pai
INSERT INTO mentorshipMatch (matchID, menteeID, mentorID)
VALUES (DEFAULT, 00000000789, 00000000456);

DELETE
FROM mentorshipMatch
WHERE matchID = 00000000001
  AND mentorID = 00000000456;

--------------- PERSONA 2
---------------

-- 2.1: ask a question about future global experience
INSERT INTO Question(qID, sID, content, isApproved)
VALUES (00000000003, 00000000101, 'What should I pack for a semester in Rome?', 1);

SELECT *
From Question
WHERE sID = 00000000101;

UPDATE Question
SET isApproved = 1
WHERE qID = 00000000003;

DELETE
FROM Question
where qID = 00000000003;

-- 2.2: search for location based on my major
SELECT l.locationID, l.city, l.country, ap.programName, ap.prgmDescription
FROM Location l
         JOIN abroadProgram ap ON l.locationID = ap.locationID
         JOIN Major m ON m.majorID = 00000000002
ORDER BY l.city;

-- 2.3: question the global experience office
INSERT INTO Question (qID, sID, content, datePosted, isApproved)
VALUES (00000000003, 00000000202, 'Do I get to choose my roommate?', DEFAULT, 1);

-- 2.4: view  the replies to a question
SELECT q.content, r.replyID, r.sID, r.qID, r.datePosted, r.isApproved
FROM Question q
         JOIN Reply r ON q.qID = r.qID
WHERE q.qID = 00000000001;

-- 2.5: view rating on specific locations
SELECT l.city,
       l.country,
       p.fName,
       p.lName,
       r.locRating,
       r.profRating,
       r.avgRating,
       r.comment
FROM Rating r
         JOIN Location l ON r.locRating = l.locationID
         JOIN Professor p ON r.profRating = p.profID
WHERE r.sID = 00000000303;

-- 2.6: find another student going to the same location
SELECT s.fName, s.lName, s.email, p.programName, l.city, l.country
FROM Student s
         JOIN studentAbroadProgram sap ON s.sID = sap.sID
         JOIN abroadProgram p ON sap.programID = p.programID
         JOIN Location l ON p.locationID = l.locationID
WHERE l.locationID = 00000000001
  AND s.sID != 00000000101
ORDER BY s.fName, s.lName;

--------------- PERSONA 3
---------------

-- 3.1: Deleting/limiting comments
DELETE
FROM Reply
WHERE isApproved = 0;

-- 3.2: Maintaining locations
INSERT INTO Location(locationID, city, country, description)
VALUES (3, 'Bangkok', 'Thailand', 'Bangkok, the vibrant capital of Thailand, is a bustling metropolis known for its ornate temples, lively street markets, and dynamic nightlife. The city blends traditional culture with modernity, offering a mix of historic sites, shopping districts, and world-class dining experiences.');

-- 3.3: Moderate a rating system for courses & professors
SELECT *
FROM Rating
WHERE profRating = 4;

-- 3.4: Moderate a rating system for accomodations and lifestyle
UPDATE Rating
SET locRating = 3,
    comment   = 'Great environment for keeping up with athletic habits. May not be suitable for those not accustomed to routine physical activity.'
WHERE ratingID = 00000000001;

-- 3.5: Moderate a rating system for location
DELETE
FROM Rating
WHERE ratingID = 00000000002;

-- 3.6: Creating/maintaining forum posts
UPDATE Reply
SET content = 'Updated reply content here.'
WHERE replyID = 00000000001;

--------------- PERSONA 4
---------------

-- 4.1: update resources for specific loc
UPDATE Resources
SET category = 'Updated Housing Information'
WHERE locationID = 1;

-- 4.2: retrieve real-time feedback on housing, professors, and local services
-- in order of most recent to least recent
SELECT locRating, profRating, comment, datePosted
FROM Rating
WHERE programID = 1
ORDER BY datePosted DESC;

-- 4.3: track app usage over monthly periods
SELECT empID, featureID, usageCount, DATE_FORMAT(date, '%Y-%m') AS usageMonth
FROM engagementAnalytics
WHERE date >= '2023-11-18'
GROUP BY empID, featureID, usageMonth
ORDER BY usageMonth DESC;

-- 4.4: moderate alerts
INSERT INTO Alerts(alertID, locationID, message)
VALUES (5, 1, 'Record high temperatures today, stay hydrated!');

-- 4.5: moderate students
INSERT INTO Student(sID, fName, lName, email, majorID, blurb, role, programID)
VALUES (5, 'Melody', 'Green', 'melodygreen@gmail.com', 2,
        'Hi! Im a second year student who just returned from Rome and want to be your mentor!',
        'mentor', 1);

-- 4.6: control resources
DELETE
FROM Resources
WHERE resourceID = 2;
CREATE TABLE IF NOT EXISTS abroadProgram
(
    programID       INT(11) UNIQUE PRIMARY KEY,
    programName     VARCHAR(100)   NOT NULL,
    prgmDescription LONGTEXT       NOT Null,
    locationID      INT(11) UNIQUE NOT NULL,
    programType     VARCHAR(100)   NOT NULL,
    empID           INT(11) UNIQUE NOT NULL,
    CONSTRAINT ap_fk_01 FOREIGN KEY (programID)
        REFERENCES employeeAbroadProgram (programID)

);