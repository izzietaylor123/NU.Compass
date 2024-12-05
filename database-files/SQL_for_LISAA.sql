-- SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0;
-- SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0;
-- SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'TRADITIONAL,ALLOW_INVALID_DATES';

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
    empID           INT(11)  NOT NULL,
    CONSTRAINT location_fk FOREIGN KEY (locationID)
        REFERENCES Location (locationID)
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
        REFERENCES abroadProgram (programID),
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
);

DROP TABLE IF EXISTS Professor;
CREATE TABLE IF NOT EXISTS Professor
(
    profID     INT(11)      NOT NULL AUTO_INCREMENT,
    fName      VARCHAR(200) NOT NULL,
    lName      VARCHAR(200) NOT NULL,
    department VARCHAR(200),
    email      VARCHAR(200),
    PRIMARY KEY (profID)
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
        REFERENCES abroadProgram (programID),
    CONSTRAINT professor_fk_01 FOREIGN KEY (professorID)
        REFERENCES Professor (profID)
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
    UNIQUE(empID),
    CONSTRAINT course_fk_02 FOREIGN KEY (courseID)
        REFERENCES Course (courseID)
);

DROP TABLE IF EXISTS employeeAbroadProgram;
CREATE TABLE IF NOT EXISTS employeeAbroadProgram
(
    programID INT(11) NOT NULL,
    empID     INT(11) NOT NULL,
    PRIMARY KEY (programID, empID),
    CONSTRAINT eap_pk_00 FOREIGN KEY (programID)
        REFERENCES abroadProgram (programID),
    CONSTRAINT eap_pk_01 FOREIGN KEY (empID)
        REFERENCES adminEmployee (empID)
);

DROP TABLE IF EXISTS engagementAnalytics;
CREATE TABLE IF NOT EXISTS engagementAnalytics
(
    featureID  INT(11) PRIMARY KEY AUTO_INCREMENT,
    empID      INT(11)  NOT NULL,
    usageCount INT      NOT NULL,
    date       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    feature VARCHAR(50),
    CONSTRAINT eng_analytics_fk_01 FOREIGN KEY (empID)
        REFERENCES adminEmployee (empID)
);







DROP TABLE IF EXISTS studentAbroadProgram;
CREATE TABLE IF NOT EXISTS studentAbroadProgram
(
    programID INT(11) NOT NULL,
    sID       INT(11) NOT NULL,
    PRIMARY KEY (programID, sID),
    CONSTRAINT sap_pk_00 FOREIGN KEY (programID)
        REFERENCES abroadProgram (programID),
    CONSTRAINT sap_pk_01 FOREIGN KEY (sID)
        REFERENCES Student (sID)
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
        REFERENCES Major (majorID),
    CONSTRAINT sm_pk_01 FOREIGN KEY (sID)
        REFERENCES Student (sID)
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
    replyID    INT(11) NOT NULL AUTO_INCREMENT,
    sID        INT(11) NOT NULL,
    qID        INT(11) NOT NULL,
    content    VARCHAR(2000),
    datePosted DATETIME DEFAULT CURRENT_TIMESTAMP,
    isApproved BOOLEAN,
    PRIMARY KEY (replyID),
    CONSTRAINT reply_fk_01 FOREIGN KEY (sID)
        REFERENCES Student (sID),
    CONSTRAINT reply_fk_02 FOREIGN KEY (qID)
        REFERENCES Question (qID)
);


-- Location Data
INSERT INTO Location (locationID, city, country, description) VALUES
(1, 'Vienna', 'Austria', 'The capital city known for its cultural events, imperial sites, and coffee houses.'),
(2, 'Brussels', 'Belgium', 'The heart of the European Union and famous for its chocolates and beers.'),
(3, 'Copenhagen', 'Denmark', 'A charming capital with a historic center, modern architecture, and culinary scene.'),
(4, 'Helsinki', 'Finland', 'A vibrant seaside city with unique architecture and design.'),
(5, 'Paris', 'France', 'The city of love and the Eiffel Tower, known for its art, fashion, and gastronomy.'),
(6, 'Berlin', 'Germany', 'A city rich in history with modern architecture and vibrant arts scene.'),
(7, 'Athens', 'Greece', 'The cradle of Western civilization, known for its ancient monuments.'),
(8, 'Dublin', 'Ireland', 'The capital city known for its cultural heritage and vibrant nightlife.'),
(9, 'Rome', 'Italy', 'The Eternal City, renowned for its ancient history and architecture.'),
(10, 'Amsterdam', 'Netherlands', 'A city with scenic canals, artistic heritage, and vibrant cycling culture.'),
(11, 'Oslo', 'Norway', 'A modern city in the midst of stunning natural beauty.'),
(12, 'Warsaw', 'Poland', 'A city that blends a rich history with a contemporary urban cultural scene.'),
(13, 'Lisbon', 'Portugal', 'A hilly coastal city with a rich maritime history and a vibrant cultural scene.'),
(14, 'Madrid', 'Spain', 'The bustling capital known for its cultural festivals, art museums, and tapas.'),
(15, 'Stockholm', 'Sweden', 'A city spread across 14 islands with a rich history and vibrant urban life.'),
(16, 'Bern', 'Switzerland', 'The de facto capital known for its medieval architecture and charm.'),
(17, 'London', 'United Kingdom', 'A world-leading global city known for its history, arts, and multicultural landscape.'),
(18, 'Barcelona', 'Spain', 'Known for its unique architecture, vibrant nightlife, and stunning beaches.'),
(19, 'Munich', 'Germany', 'Famous for its Oktoberfest, beer gardens, and cultural heritage.'),
(20, 'Stuttgart', 'Germany', 'A city surrounded by vineyards, famous for automotive industry giants.'),
(21, 'Frankfurt', 'Germany', 'A leading financial hub with a skyline filled with skyscrapers.'),
(22, 'Hamburg', 'Germany', 'A harbor city known for its maritime culture and musical heritage.'),
(23, 'Cologne', 'Germany', 'Known for its impressive cathedral and vibrant media and tourism industries.'),
(24, 'Düsseldorf', 'Germany', 'Recognized for its fashion industry and art scene.'),
(25, 'Leipzig', 'Germany', 'Celebrated for its music, art, and its role in history as a trade city.'),
(26, 'Bordeaux', 'France', 'World-famous for its wine and stunning 18th-century architecture.'),
(27, 'Nice', 'France', 'Known for its beautiful Mediterranean beaches and vibrant cultural life.'),
(28, 'Lyon', 'France', 'Known for its historical and architectural landmarks and gastronomy.'),
(29, 'Marseille', 'France', 'A port city with a rich maritime history and multicultural vibe.'),
(30, 'Naples', 'Italy', 'Renowned for its rich history, art, gastronomy, and the nearby Amalfi Coast.'),
(31, 'Oakland', 'United States', 'Nestled between the coast and Silicon Valley, Oakland is the perfect mix of business and pleasure.');

-- abroadProgram Data
INSERT INTO abroadProgram (programID, programName, prgmDescription, locationID, programType, empID) VALUES
(1, 'Vienna', 'Experience innovation in Vienna with a focus on startups, venture capital, and entrepreneurship.', 1, 'Dialogue of Civilizations', 1),
(2, 'Brussels', 'Immerse yourself in the healthcare system of Brussels, with practical sessions in public health and medical ethics.', 2, 'Semester.in', 2),
(3, 'Copenhagen', 'Investigate the advancements in AI and robotics in Copenhagen, alongside industry leaders and academic mentors.', 3, 'Traditional Study Abroad', 3),
(4, 'Helsinki', 'Analyze the economic landscape of Helsinki while studying international economics and development.', 4, 'Traditional Study Abroad', 4),
(5, 'Paris', 'Live and learn in Paris while exploring central and Western European studies through a historical lens.', 5, 'Semester.in', 5),
(6, 'Berlin', 'Experience the unique blend of tradition and modernity in Berlin with courses in history, culture, and politics.', 6, 'Traditional Study Abroad', 6),
(7, 'Athens', 'Study marine biology in the coastal city of Athens and engage with local conservation projects.', 7, 'Dialogue of Civilizations', 7),
(8, 'Dublin', 'Study the art and architecture of Dublin while taking courses in design thinking and innovation.', 8, 'NU.in', 8),
(9, 'Rome', 'Witness the urban evolution of Rome and study urban planning, real estate, and architecture.', 9, 'Dialogue of Civilizations', 9),
(10, 'Amsterdam', 'Participate in our intensive studies program in Amsterdam, focusing on history, politics, and contemporary culture.', 10, 'Traditional Study Abroad', 10),
(11, 'Oslo', 'Analyze the economic landscape of Oslo while studying international economics and development.', 11, 'Traditional Study Abroad', 11),
(12, 'Warsaw', 'Engage with the community development efforts in Warsaw while studying sociology and humanitarian action.', 12, 'Dialogue of Civilizations', 12),
(13, 'Lisbon', 'Experience the vibrant city life of Lisbon and study Portuguese language and culture through hands-on projects.', 13, 'NU.in', 13),
(14, 'Madrid', 'Witness the urban evolution of Madrid and study urban planning, real estate, and architecture.', 14, 'Dialogue of Civilizations', 14),
(15, 'Stockholm', 'Immerse yourself in the healthcare system of Stockholm, with practical sessions in public health and medical ethics.', 15, 'Dialogue of Civilizations', 15),
(16, 'Bern', 'Participate in wildlife conservation efforts in Bern, focusing on ecosystem management and biology studies.', 16, 'Traditional Study Abroad', 16),
(17, 'London', 'Experience innovation in London with a focus on startups, venture capital, and entrepreneurship.', 17, 'Traditional Study Abroad', 17),
(18, 'Barcelona', 'Discover the ancient history of Barcelona while participating in archaeological digs and classical studies.', 18, 'NU.in', 18),
(19, 'Munich', 'Dive into the history and business environment of Munich with a focus on international finance and management practices.', 19, 'NU.in', 19),
(20, 'Stuttgart', 'Engage with the community development efforts in Stuttgart while studying sociology and humanitarian action.', 20, 'Dialogue of Civilizations', 20),
(21, 'Frankfurt', 'Participate in a comprehensive language and culture program in Frankfurt, offering insights into Vietnam''s rapid growth.', 21, 'Traditional Study Abroad', 21),
(22, 'Hamburg', 'Experience Hamburg through the lens of political science and economics, understanding the Latin American context.', 22, 'Semester.in', 22),
(23, 'Cologne', 'Participate in wildlife conservation efforts in Cologne, focusing on ecosystem management and biology studies.', 23, 'Dialogue of Civilizations', 23),
(24, 'Düsseldorf', 'Experience innovation in Düsseldorf with a focus on startups, venture capital, and entrepreneurship.', 24, 'Dialogue of Civilizations', 24),
(25, 'Leipzig', 'Study fashion and culture in the bustling city of Leipzig, a global hub for design and creativity.', 25, 'Traditional Study Abroad', 25),
(26, 'Bordeaux', 'Participate in Bordeaux''s economic growth story with a focus on entrepreneurship and international business.', 26, 'Semester.in', 26),
(27, 'Nice', 'Explore Nice''s approach to sustainability with courses in renewable energy and environmental management.', 27, 'Traditional Study Abroad', 27),
(28, 'Lyon', 'Dive into the rich cultural scene of Lyon with courses in music, history, and the arts.', 28, 'NU.in', 28),
(29, 'Marseille', 'Study fashion and culture in the bustling city of Marseille, a global hub for design and creativity.', 29, 'Dialogue of Civilizations', 29),
(30, 'Naples', 'Experience the unique blend of tradition and modernity in Naples with courses in history, culture, and politics.', 30, 'Traditional Study Abroad', 30),
-- abroadProgram #31 should not have any connected ratings or questions, and will test how the program reacts to empty json calls
(31, 'Oakland', 'Explore your academic interests on our sunny California campus!', 31, 'Semester.in', 30);

-- Student Data
INSERT INTO Student (sID, fName, lName, email, blurb, role) VALUES
(1, 'Aeriel', 'Sommerton', 'aeriel.sommerton@web.de',  'Dance is my outlet for energy and creativity. I practice various styles and perform in competitions, always striving to learn new choreography.', 'mentor'),
(2, 'Meaghan', 'Le Ball', 'meaghan.leball@hotmail.com',  'Cooking and experimenting with new recipes is what I love most. I often host dinner parties for my friends to try out new dishes.', 'mentor'),
(3, 'Ondrea', 'Kinsella', 'ondrea.kinsella@yahoo.co.in',  'Video games are my favorite pastime. I enjoy strategy games that challenge my mind and continuously seek to improve my skills.', 'mentor'),
(4, 'Kile', 'McPhelimey', 'kile.mcphelimey@libero.it',  'Dance is my outlet for energy and creativity. I practice various styles and perform in competitions, always striving to learn new choreography.', 'mentor'),
(5, 'Ash', 'Uff', 'ash.uff@hotmail.com',  'Math challenges and numbers are where I find solace. Sudoku and puzzles occupy my free time, alongside participating in national math competitions.', 'mentor'),
(6, 'Shelli', 'Milius', 'shelli.milius@neuf.fr',  'I have a passion for mathematics and spend most of my time solving complex equations. Outside of academics, I enjoy playing chess and competing in local tournaments.', 'mentor'),
(7, 'Fayth', 'Sodor', 'fayth.sodor@gmx.de',  'Dance is my outlet for energy and creativity. I practice various styles and perform in competitions, always striving to learn new choreography.', 'mentor'),
(8, 'Nahum', 'Seeler', 'nahum.seeler@wanadoo.fr',  'Video games are my favorite pastime. I enjoy strategy games that challenge my mind and continuously seek to improve my skills.', 'mentor'),
(9, 'Scotti', 'Rivallant', 'scotti.rivallant@gmail.com',  'I enjoy writing and have a blog where I share book reviews and personal thoughts. Connecting with readers from around the world is enriching.', 'mentor'),
(10, 'Cosme', 'Elliot', 'cosme.elliot@yahoo.com',  'Science is my favorite subject, especially biology. Exploring the natural world and understanding how things work piques my interest like nothing else!', 'mentor'),
(11, 'Goldy', 'Evesque', 'goldy.evesque@gmail.com',  'I am an avid reader and love diving into fantasy novels. When I am not studying, you can find me writing short stories or exploring new coffee shops around town.', 'mentor'),
(12, 'Court', 'Gildroy', 'court.gildroy@gmail.com', 'Music runs in my family, and I play the guitar in a band with my friends. On weekends, we perform at local gigs, bringing energy to the stage.', 'mentor'),
(13, 'Mahala', 'Boerderman', 'mahala.boerderman@gmail.com',  'Technology and coding are my main interests. I spend weekends participating in hackathons and building apps to solve everyday problems.', 'mentor'),
(14, 'Avrom', 'Nilges', 'avrom.nilges@gmail.com',  'Social justice is close to my heart, and I volunteer at a local community center. Advocating for change and helping others drives me.', 'mentor'),
(15, 'Charin', 'Boggish', 'charin.boggish@yahoo.co.id',  'Video games are my favorite pastime. I enjoy strategy games that challenge my mind and continuously seek to improve my skills.', 'mentor'),
(16, 'Wallie', 'Sandon', 'wallie.sandon@yahoo.com',  'Outdoor adventures are what I live for. Whether it is hiking, camping, or rock climbing, being in nature gives me peace and brings out the best in me.', 'mentee'),
(17, 'Ryun', 'Athy', 'ryun.athy@hotmail.com',  'Technology and coding are my main interests. I spend weekends participating in hackathons and building apps to solve everyday problems.', 'mentee'),
(18, 'Gates', 'Ledeker', 'gates.ledeker@gmail.com',  'Acting is my passion, and I participate in school plays and local theater productions. I thrive on stage and love bringing characters to life.', 'mentee'),
(19, 'Bliss', 'Conibear', 'bliss.conibear@freenet.de',   'Social justice is close to my heart, and I volunteer at a local community center. Advocating for change and helping others drives me.', 'mentee'),
(20, 'Carny', 'Huniwall', 'carny.huniwall@gmail.com',  'Cooking and experimenting with new recipes is what I love most. I often host dinner parties for my friends to try out new dishes.', 'mentee'),
(21, 'Vyky', 'Worsnip', 'vyky.worsnip@hotmail.com',  'I have a passion for mathematics and spend most of my time solving complex equations. Outside of academics, I enjoy playing chess and competing in local tournaments.', 'mentee'),
(22, 'Trenna', 'Gerbel', 'trenna.gerbel@hotmail.com',  'I am an avid reader and love diving into fantasy novels. When I am not studying, you can find me writing short stories or exploring new coffee shops around town.', 'mentee'),
(23, 'Ebonee', 'Halkyard', 'ebonee.halkyard@yahoo.com.br',  'Photography helps me capture the world from different perspectives. Whether it is landscagit pes or portraits, I love finding beauty in everyday life.', 'mentee'),
(24, 'Keenan', 'Mowson', 'keenan.mowson@yahoo.com',  'I enjoy writing and have a blog where I share book reviews and personal thoughts. Connecting with readers from around the world is enriching.', 'mentee'),
(25, 'Yorke', 'Bensusan', 'yorke.bensusan@sbcglobal.net',  'Sports are my life! I am the captain of the soccer team and love spending my afternoons practicing or watching matches with friends.', 'mentee'),
(26, 'Wilton', 'Worsell', 'wilton.worsell@yahoo.fr',  'Math challenges and numbers are where I find solace. Sudoku and puzzles occupy my free time, alongside participating in national math competitions.', 'mentee'),
(27, 'Alayne', 'Whitnell', 'alayne.whitnell@yahoo.com',  'Math challenges and numbers are where I find solace. Sudoku and puzzles occupy my free time, alongside participating in national math competitions.', 'mentee'),
(28, 'Fanchon', 'Quarry', 'fanchon.quarry@hotmail.com',  'Video games are my favorite pastime. I enjoy strategy games that challenge my mind and continuously seek to improve my skills.', 'mentee'),
(29, 'Cahra', 'Wooster', 'cahra.wooster@wanadoo.fr',   'Acting is my passion, and I participate in school plays and local theater productions. I thrive on stage and love bringing characters to life.', 'mentee'),
(30, 'Amy', 'McAviy', 'amy.mcaviy@msn.com', 'Outdoor adventures are what I live for. Whether it is hiking, camping, or rock climbing, being in nature gives me peace and brings out the best in me.', 'mentee'),
(31, 'Tim', 'Waltz', 't.waltz@northeastern.edu', 'I am a second-year Northeastern student studying Business who recently returned from my transformative Dialogue of Civilizations in Marseille, France. When I am not mentoring, I enjoy tennis, Stardew Valley, and chocolate chip cookies.  I look forward to connecting with you, feel free to reach out to me at w.tim@northeastern.edu!', 'mentor'),
(32, 'Tom', 'Holland', 't.holland@northeastern.edu', 'I am a Northeastern Business student looking to go on a Dialogue of Civilations for business! Looking for mentors!', 'mentee');


-- Ratings Data
INSERT INTO Rating (ratingID, programID, sID, datePosted, locRating, profRating, atmosphereRating, comment) VALUES
(1, 1, 1, '2024-01-15', 5, 5, 4, 'Great program! The organization and content exceeded my expectations.'),
(2, 2, 2, '2024-02-10', 4, 3, 4, 'The program was informative but could use more hands-on activities.'),
(3, 3, 3, '2024-03-05', 5, 5, 5, 'Excellent experience with knowledgeable mentors and engaging sessions.'),
(4, 4, 4, '2024-03-20', 3, 4, 4, 'I enjoyed the cultural immersion, but the schedule was too packed.'),
(5, 5, 5, '2024-04-15', 4, 3, 3, 'The program was insightful, but some topics lacked depth.'),
(6, 6, 6, '2024-05-10', 5, 5, 5, 'Amazing opportunity to learn and grow, well-structured sessions.'),
(7, 7, 7, '2024-05-25', 5, 5, 5, 'The program was fantastic, and the location was stunning!'),
(8, 8, 8, '2024-06-15', 3, 4, 3, 'Informative but lacked diversity in perspectives.'),
(9, 9, 9, '2024-06-30', 5, 5, 5, 'Engaging program with excellent networking opportunities.'),
(10, 10, 10, '2024-07-10', 5, 5, 4, 'Very detailed and comprehensive, highly recommend.'),
(11, 11, 11, '2024-07-25', 4, 3, 3, 'Good content but too theoretical for my liking.'),
(12, 12, 12, '2024-08-10', 5, 4, 4, 'Well-organized with great cultural experiences.'),
(13, 13, 13, '2024-08-25', 5, 5, 5, 'Fantastic mentorship and real-world applications.'),
(14, 14, 14, '2024-09-15', 3, 4, 3, 'The program lacked structure but had good content.'),
(15, 15, 15, '2024-09-30', 4, 4, 4, 'Great program for learning new skills.'),
(16, 16, 1, '2024-10-10', 5, 5, 5, 'Very immersive and hands-on experience.'),
(17, 17, 2, '2024-10-25', 5, 5, 5, 'I learned a lot and met some amazing people!'),
(18, 18, 3, '2024-11-10', 4, 4, 4, 'The program was interesting but lacked advanced topics.'),
(19, 19, 4, '2024-11-25', 5, 5, 5, 'Great insights into the field and career opportunities.'),
(20, 20, 5, '2024-12-05', 4, 4, 4, 'The program was enjoyable but could be more organized.'),
(21, 21, 6, '2024-12-15', 5, 5, 5, 'Excellent program with a supportive team.'),
(22, 22, 7, '2024-12-20', 4, 4, 4, 'Very insightful but needed more practical applications.'),
(23, 23, 8, '2025-01-05', 5, 5, 5, 'Amazing experience, highly recommend.'),
(24, 24, 9, '2025-01-15', 4, 4, 4, 'Good balance between theory and practice.'),
(25, 25, 10, '2025-01-25', 4, 4, 4, 'The program was too short but very engaging.'),
(26, 26, 11, '2025-02-05', 3, 3, 3, 'Great location but the sessions were repetitive.'),
(27, 27, 12, '2025-02-15', 5, 5, 5, 'Fantastic program with excellent facilities.'),
(28, 28, 13, '2025-02-25', 4, 4, 4, 'Enjoyable program with knowledgeable speakers.'),
(29, 29, 14, '2025-03-05', 5, 5, 5, 'I gained valuable knowledge and skills.'),
(30, 30, 15, '2025-03-15', 3, 4, 3, 'The program was good but needed more activities.'),
(31, 29, 31, '2025-03-15', 3, 4, 3, 'The program was good but needed more activities.');



-- Alerts Data
INSERT INTO Alerts (alertID, locationID, message, datePosted) VALUES
(1, 1, 'Water supply interruption scheduled for tomorrow between 9 AM and 4 PM.', '2024-05-04 01:22:10'),
(2, 2, 'Flash flood warning in effect. Avoid low-lying areas and seek higher ground.', '2024-09-28 00:58:59'),
(3, 3, 'Transportation strike announced. Expect disruptions in public transit services.', '2024-08-07 18:26:35'),
(4, 4, 'Lightning warning issued. Stay indoors and avoid open fields or elevated places.', '2024-07-19 01:25:56'),
(5, 5, 'Reminder: Curfew in place from 11 PM to 5 AM for safety reasons.', '2024-06-27 04:47:44'),
(6, 6, 'Cultural event postponed due to organizer issues. New date to be announced soon.', '2024-03-29 18:30:26'),
(7, 7, 'Sudden drop in temperature expected tonight. Dress warmly and take precautions for icy roads.', '2023-12-31 06:05:33'),
(8, 8, 'Typhoon warning: Stock up on essentials and stay updated on weather conditions.', '2024-03-06 07:23:30'),
(9, 9, 'Sudden drop in temperature expected tonight. Dress warmly and take precautions for icy roads.', '2024-01-19 03:21:08'),
(10, 10, 'Sudden drop in temperature expected tonight. Dress warmly and take precautions for icy roads.', '2024-01-18 06:28:30'),
(11, 11, 'Extreme heat alert issued. Cooling centers available at designated locations.', '2024-03-25 07:58:39'),
(12, 12, 'Sudden drop in temperature expected tonight. Dress warmly and take precautions for icy roads.', '2024-11-01 18:18:34'),
(13, 13, 'Concert in the park cancelled due to unexpected weather conditions.', '2023-12-14 18:14:30'),
(14, 14, 'Concert in the park cancelled due to unexpected weather conditions.', '2024-07-18 06:05:14'),
(15, 15, 'Transportation strike announced. Expect disruptions in public transit services.', '2024-10-04 14:29:30'),
(16, 16, 'Security incident reported in the vicinity. Avoid the area and follow local guidance.', '2024-07-24 12:38:42'),
(17, 17, 'Classes moved online due to power outage. Check your email for further instructions.', '2024-06-01 07:23:51'),
(18, 18, 'Online scam alert: Be wary of unsolicited emails asking for personal information.', '2024-07-25 06:43:10'),
(19, 19, 'Protest march expected downtown. Plan your travel accordingly and avoid affected roads.', '2024-08-02 11:59:43'),
(20, 20, 'Fire drill scheduled for 3 PM today. Proceed to the nearest exit when alarm sounds.', '2024-09-24 21:23:03'),
(21, 21, 'Air quality alert: High levels of pollution expected. Limit outdoor activities.', '2024-08-01 09:47:45'),
(22, 22, 'Water supply interruption scheduled for tomorrow between 9 AM and 4 PM.', '2024-09-15 13:43:16'),
(23, 23, 'Concert in the park cancelled due to unexpected weather conditions.', '2024-07-09 07:07:52'),
(24, 24, 'Sudden drop in temperature expected tonight. Dress warmly and take precautions for icy roads.', '2024-05-08 04:09:08'),
(25, 25, 'Sudden drop in temperature expected tonight. Dress warmly and take precautions for icy roads.', '2024-06-09 19:03:36'),
(26, 26, 'Reminder: Curfew in place from 11 PM to 5 AM for safety reasons.', '2024-11-23 18:28:09'),
(27, 27, 'Classes moved online due to power outage. Check your email for further instructions.', '2024-03-12 20:44:01'),
(28, 28, 'Heatwave expected over the next few days. Stay hydrated and avoid excessive outdoor activities.', '2024-07-09 07:51:56'),
(29, 29, 'Transportation strike announced. Expect disruptions in public transit services.', '2024-03-24 16:08:11'),
(30, 30, 'Reminder: Curfew in place from 11 PM to 5 AM for safety reasons.', '2024-08-11 14:14:48');

-- Resources Data
INSERT INTO Resources (resourceID, locationID, category, lastUpdated)
VALUES
(1, 1, 'FAQs and Troubleshooting', '2024-09-12 18:38:19'),
(2, 2, 'Academic Information', '2024-07-06 20:13:14'),
(3, 3, 'Post-Study Abroad Resources', '2024-04-15 15:16:01'),
(4, 4, 'Travel and Exploration', '2024-03-15 17:30:38'),
(5, 5, 'Travel and Exploration', '2024-04-09 08:12:38'),
(6, 6, 'Cultural and Social Life', '2024-08-26 21:16:01'),
(7, 7, 'Local Information', '2023-12-30 02:45:31'),
(8, 8, 'Cultural and Social Life', '2024-02-26 14:34:52'),
(9, 9, 'Travel and Exploration', '2024-01-11 13:44:14'),
(10, 10, 'Technology and Communication', '2024-07-25 19:02:18'),
(11, 11, 'Health and Wellbeing', '2024-06-23 11:06:44'),
(12, 12, 'Pre-Departure Information', '2024-07-11 18:17:45'),
(13, 13, 'Health and Wellbeing', '2024-06-17 17:00:42'),
(14, 14, 'Student Services', '2024-03-24 12:51:56'),
(15, 15, 'Technology and Communication', '2024-07-24 05:29:27'),
(16, 16, 'Health and Wellbeing', '2024-01-16 18:58:02'),
(17, 17, 'Post-Study Abroad Resources', '2024-04-06 07:18:22'),
(18, 18, 'Financial Resources', '2024-07-26 08:45:26'),
(19, 19, 'Cultural and Social Life', '2024-02-23 18:19:52'),
(20, 20, 'Cultural and Social Life', '2024-06-14 11:50:40'),
(21, 21, 'Travel and Exploration', '2024-08-28 21:15:09'),
(22, 22, 'Health and Wellbeing', '2024-10-25 12:06:18'),
(23, 23, 'Cultural and Social Life', '2023-12-19 08:22:17'),
(24, 24, 'Technology and Communication', '2023-12-30 21:22:24'),
(25, 25, 'Technology and Communication', '2023-12-12 06:05:59'),
(26, 26, 'Travel and Exploration', '2024-08-31 21:42:26'),
(27, 27, 'Local Information', '2024-08-25 08:36:34'),
(28, 28, 'Travel and Exploration', '2024-01-30 02:44:18'),
(29, 29, 'Housing and Accommodation', '2024-01-16 13:09:29'),
(30, 30, 'Local Information', '2024-07-18 20:19:06');

-- Professor Data
INSERT INTO Professor (profID, fName, lName, department, email) VALUES
(1, 'Gallagher', 'Chalcroft', 'Engineering', 'gallagher.chalcroft@gmail.com'),
(2, 'Otha', 'Stoakes', 'Biology', 'otha.stoakes@yahoo.com'),
(3, 'Pearce', 'Fiddymont', 'History', 'pearce.fiddymont@yahoo.com'),
(4, 'Teador', 'Brim', 'History', 'teador.brim@gmail.com'),
(5, 'Diana', 'Greenroyd', 'Mathematics', 'diana.greenroyd@yahoo.com'),
(6, 'Ignacio', 'Mapplethorpe', 'Physics', 'ignacio.mapplethorpe@t-online.de'),
(7, 'Lonnard', 'Cristofolini', 'Computer Science', 'lonnard.cristofolini@yahoo.com'),
(8, 'Cecilio', 'Dowbekin', 'Political Science', 'cecilio.dowbekin@yahoo.fr'),
(9, 'Trisha', 'Bernot', 'Chemistry', 'trisha.bernot@hotmail.fr'),
(10, 'Ariana', 'Jobbins', 'Psychology', 'ariana.jobbins@yahoo.com.br'),
(11, 'Norton', 'Fahy', 'Mathematics', 'norton.fahy@yahoo.com'),
(12, 'Nanci', 'Snowling', 'Mathematics', 'nanci.snowling@yahoo.com'),
(13, 'Koren', 'Ramelot', 'History', 'koren.ramelot@yahoo.com'),
(14, 'Lester', 'Domnin', 'Art History', 'lester.domnin@hotmail.com'),
(15, 'Maridel', 'Pinke', 'Computer Science', 'maridel.pinke@gmail.com'),
(16, 'Margaretha', 'Worsfold', 'History', 'margaretha.worsfold@yahoo.com'),
(17, 'Timi', 'Scirman', 'Psychology', 'timi.scirman@yahoo.com'),
(18, 'Lucais', 'Schankelborg', 'Sociology', 'lucais.schankelborg@gmail.com'),
(19, 'Donnajean', 'Grumble', 'Art History', 'donnajean.grumble@wanadoo.fr'),
(20, 'Jonah', 'Westerman', 'Economics', 'jonah.westerman@gmail.com'),
(21, 'Judah', 'Elintune', 'Psychology', 'judah.elintune@gmail.com'),
(22, 'Ricard', 'Woolveridge', 'English', 'ricard.woolveridge@hotmail.com'),
(23, 'Briney', 'Marvelley', 'Architecture', 'briney.marvelley@yahoo.com'),
(24, 'Stanford', 'Ledster', 'Architecture', 'stanford.ledster@hotmail.com'),
(25, 'Normy', 'Davidowich', 'Architecture', 'normy.davidowich@live.com'),
(26, 'Addison', 'de Bullion', 'Biology', 'addison.debullion@yahoo.com'),
(27, 'Almeria', 'Goodridge', 'Sociology', 'almeria.goodridge@yahoo.es'),
(28, 'Cherrita', 'Alelsandrowicz', 'Chemistry', 'cherrita.alelsandrowicz@gmail.com'),
(29, 'Linc', 'Reynoollds', 'History', 'linc.reynoollds@gmail.com'),
(30, 'Averyl', 'Harmer', 'English', 'averyl.harmer@yahoo.com.br'),
(31, 'Janene', 'Bramhall', 'Mathematics', 'janene.bramhall@yahoo.fr'),
(32, 'Meggi', 'Ackrill', 'Economics', 'meggi.ackrill@yahoo.de'),
(33, 'Christos', 'Immins', 'Computer Science', 'christos.immins@hotmail.com'),
(34, 'Elias', 'Lepoidevin', 'Economics', 'elias.lepoidevin@hotmail.com'),
(35, 'Drucy', 'Howey', 'Computer Science', 'drucy.howey@gmail.com'),
(36, 'Brandon', 'Doore', 'Economics', 'brandon.doore@yahoo.com'),
(37, 'Marleah', 'Parton', 'Architecture', 'marleah.parton@yahoo.com'),
(38, 'Niel', 'Shelsher', 'Psychology', 'niel.shelsher@yahoo.fr'),
(39, 'Abby', 'Hubbucks', 'English', 'abby.hubbucks@gmail.com'),
(40, 'Sibeal', 'Gargett', 'Sociology', 'sibeal.gargett@hotmail.com');


-- Courses Data
INSERT INTO Course (courseID, courseName, courseDescription, programID, professorID) VALUES
(1, 'World History: Ancient to Medieval', 'Examine the major civilizations, events, and cultural developments from the ancient world to the medieval period.', 1, 1),
(2, 'Introduction to Literature', 'Analyze various literary forms, themes, and techniques, exploring works from diverse periods and cultures.', 2, 2),
(3, 'Introduction to Psychology', 'Explore the fundamentals of human behavior, thought processes, and emotions through scientific research and analysis.', 3, 3),
(4, 'Introduction to Psychology', 'Explore the fundamentals of human behavior, thought processes, and emotions through scientific research and analysis.', 4, 4),
(5, 'Calculus I', 'Study the concepts of limits, derivatives, and integrals, laying the foundation for advanced mathematical courses.', 5, 5),
(6, 'Principles of Economics', 'Learn the basics of micro and macroeconomic theory and analysis, focusing on how markets function and economies operate.', 6, 6),
(7, 'Physics I: Mechanics', 'Explore the basic principles of physics with a focus on motion, forces, and energy.', 7, 7),
(8, 'Psychology of Learning', 'Delve into the theories and applications of how humans learn and retain information.', 8, 8),
(9, 'Introduction to Sociology', 'Understand the social world and human behavior in a societal context, examining social institutions and relationships.', 9, 9),
(10, 'Introduction to Psychology', 'Explore the fundamentals of human behavior, thought processes, and emotions through scientific research and analysis.', 10, 10),
(11, 'Art History: Renaissance to Modern', 'Study significant movements in art from the Renaissance to modern times, understanding historical context and artistic techniques.', 11, 11),
(12, 'Introduction to Political Science', 'Explore the fundamentals of political systems, theories, and the role of government in society.', 12, 12),
(13, 'Human Anatomy and Physiology', 'Study the structure and function of the human body, covering the major systems and organs.', 13, 13),
(14, 'Biology 101', 'Discover the principles of biology, covering cell structure, functions, genetics, evolution, and ecology.', 14, 14),
(15, 'Introduction to Literature', 'Analyze various literary forms, themes, and techniques, exploring works from diverse periods and cultures.', 15, 15),
(16, 'General Chemistry', 'Learn the foundational principles of chemistry including atomic structure, chemical bonding, and reactions.', 16, 16),
(17, 'Introduction to Philosophy', 'Examine the central questions of existence, knowledge, and ethics from various philosophical perspectives.', 17, 17),
(18, 'World History: Ancient to Medieval', 'Examine the major civilizations, events, and cultural developments from the ancient world to the medieval period.', 18, 18),
(19, 'Calculus I', 'Study the concepts of limits, derivatives, and integrals, laying the foundation for advanced mathematical courses.', 19, 19),
(20, 'Business Administration Fundamentals', 'Understand the basic principles of business operations, management, and organizational structure.', 20, 20),
(21, 'Human Anatomy and Physiology', 'Study the structure and function of the human body, covering the major systems and organs.', 21, 21),
(22, 'Environmental Science', 'Understand the interaction between humans and the environment, focusing on ecological processes and sustainability.', 22, 22),
(23, 'Modern World Literature', 'Study literary works from the 20th and 21st centuries across various cultures, focusing on themes and narrative forms.', 23, 23),
(24, 'Introduction to Literature', 'Analyze various literary forms, themes, and techniques, exploring works from diverse periods and cultures.', 24, 24),
(25, 'Statistics', 'Learn the basic principles of statistical analysis, focusing on data interpretation and probability theory.', 25, 25),
(26, 'Principles of Economics', 'Learn the basics of micro and macroeconomic theory and analysis, focusing on how markets function and economies operate.', 26, 26),
(27, 'Art History: Renaissance to Modern', 'Study significant movements in art from the Renaissance to modern times, understanding historical context and artistic techniques.', 27, 27),
(28, 'Psychology of Learning', 'Delve into the theories and applications of how humans learn and retain information.', 28, 28),
(29, 'Physics I: Mechanics', 'Explore the basic principles of physics with a focus on motion, forces, and energy.', 29, 29),
(30, 'Calculus I', 'Study the concepts of limits, derivatives, and integrals, laying the foundation for advanced mathematical courses.', 30, 30);



-- adminEmployee Data
INSERT INTO adminEmployee (empID, title, fName, lName, email, courseID) VALUES
(1, 'Software Engineer', 'Alaine', 'Hulles', 'alaine.hulles@yahoo.com', 1),
(2, 'Sales Executive', 'Berna', 'Kerr', 'berna.kerr@hotmail.com', 2),
(3, 'Manager', 'Waiter', 'Hargerie', 'waiter.hargerie@gmail.com', 3),
(4, 'Sales Executive', 'Wilfred', 'Crannage', 'wilfred.crannage@yahoo.com', 4),
(5, 'DevOps Engineer', 'Flossy', 'Hayter', 'flossy.hayter@gmail.com', 5),
(6, 'Product Owner', 'Leo', 'Foat', 'leo.foat@yahoo.com', 6),
(7, 'Product Owner', 'Shalne', 'Monkman', 'shalne.monkman@gmail.com', 7),
(8, 'Marketing Coordinator', 'Emery', 'Trundler', 'emery.trundler@me.com', 8),
(9, 'Customer Support', 'Valli', 'Hadaway', 'valli.hadaway@yahoo.com', 9),
(10, 'Marketing Coordinator', 'Kennett', 'Lappine', 'kennett.lappine@yahoo.com', 10),
(11, 'Customer Support', 'Staffard', 'Delooze', 'staffard.delooze@msn.com', 11),
(12, 'System Administrator', 'Kimberly', 'Vaune', 'kimberly.vaune@yahoo.com', 12),
(13, 'Quality Assurance', 'Sollie', 'McFadyen', 'sollie.mcfadyen@gmail.com', 13),
(14, 'UX Designer', 'Adrien', 'Ginie', 'adrien.ginie@yahoo.com', 14),
(15, 'Team Lead', 'Casi', 'Gommowe', 'casi.gommowe@sfr.fr', 15),
(16, 'Software Engineer', 'Emilia', 'Burborough', 'emilia.burborough@yahoo.com', 16),
(17, 'Quality Assurance', 'Lorrie', 'Leall', 'lorrie.leall@hotmail.com', 17),
(18, 'UX Designer', 'Forster', 'Larose', 'forster.larose@gmail.com', 18),
(19, 'HR Specialist', 'Easter', 'McLarens', 'easter.mclarens@zonnet.nl', 19),
(20, 'Product Owner', 'Buckie', 'Rowlstone', 'buckie.rowlstone@hotmail.com', 20),
(21, 'System Administrator', 'Eula', 'Casina', 'eula.casina@gmail.com', 21),
(22, 'HR Specialist', 'Harmon', 'Danser', 'harmon.danser@gmail.com', 22),
(23, 'Sales Executive', 'Berky', 'Yakunchikov', 'berky.yakunchikov@gmail.com', 23),
(24, 'Quality Assurance', 'Lara', 'Dawney', 'lara.dawney@gmail.com', 24),
(25, 'Sales Executive', 'Brenda', 'McAlroy', 'brenda.mcalroy@yahoo.com', 25),
(26, 'UX Designer', 'Lib', 'Bentick', 'lib.bentick@gmail.com', 26),
(27, 'Quality Assurance', 'Bryana', 'Beeswing', 'bryana.beeswing@gmail.com', 27),
(28, 'Product Owner', 'Guillermo', 'Ambrus', 'guillermo.ambrus@yahoo.com', 28),
(29, 'Product Owner', 'Dee', 'Feedham', 'dee.feedham@yahoo.com', 29),
(30, 'Software Engineer', 'Pattie', 'Conor', 'pattie.conor@hotmail.com', 30);


-- employeeAbroadProgram Bridge Inserts
INSERT INTO employeeAbroadProgram (programID, empID)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20),
(21, 21),
(22, 22),
(23, 23),
(24, 24),
(25, 25),
(26, 26),
(27, 27),
(28, 28),
(29, 29),
(30, 30),
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10),
(10, 11),
(11, 12),
(12, 13),
(13, 14),
(14, 15),
(15, 16),
(16, 17),
(17, 18),
(18, 19),
(19, 20),
(20, 21),
(21, 22),
(22, 23),
(23, 24),
(24, 25),
(25, 26),
(26, 27),
(27, 28),
(28, 29),
(29, 30),
(1, 3),
(2, 4),
(3, 5),
(4, 6),
(5, 7),
(6, 8),
(7, 9),
(8, 10),
(9, 11),
(10, 12),
(11, 13),
(12, 14),
(13, 15),
(14, 16),
(15, 17),
(16, 18),
(17, 19),
(18, 20),
(19, 21),
(20, 22),
(21, 23),
(22, 24),
(23, 25),
(24, 26),
(25, 27),
(26, 28),
(27, 29),
(28, 30),
(1, 4),
(2, 5),
(3, 6),
(4, 7),
(5, 8),
(6, 9),
(7, 10),
(8, 11),
(9, 12),
(10, 13),
(11, 14),
(12, 15),
(13, 16),
(14, 17),
(15, 18),
(16, 19),
(17, 20),
(18, 21),
(19, 22),
(20, 23),
(21, 24),
(22, 25),
(23, 26),
(24, 27),
(25, 28),
(26, 29),
(27, 30);


-- engagementAnalytics Data
INSERT INTO engagementAnalytics (featureID, empID, usageCount, date, feature)
VALUES
(1, 18, 174, '2024-01-30 14:48:01', 'Login'),
(2, 5, 46, '2023-12-14 16:56:09', 'Profile Update'),
(3, 3, 362, '2024-01-30 11:56:11', 'Mentorship Forum'),
(4, 18, 175, '2024-01-31 01:37:57', 'Message Center'),
(5, 5, 397, '2024-01-30 07:48:03', 'Program Rating'),
(6, 27, 262, '2024-01-30 20:20:11', 'Search Programs'),
(7, 7, 494, '2024-05-26 20:23:37', 'Resource Downloads'),
(8, 24, 533, '2024-06-10 06:03:51', 'Course Evaluations'),
(9, 30, 618, '2024-07-11 02:26:34', 'Safety Alerts'),
(10, 28, 606, '2024-07-06 18:25:53', 'Peer Reviews'),
(11, 22, 594, '2024-07-02 07:23:02', 'Dashboard Usage'),
(12, 12, 543, '2024-06-13 19:44:31', 'Event Registrations'),
(13, 8, 415, '2024-04-27 18:09:54', 'Login'),
(14, 22, 490, '2024-05-25 08:27:23', 'Profile Update'),
(15, 22, 807, '2024-12-30 07:37:54', 'Mentorship Forum'),
(16, 6, 210, '2024-02-12 20:59:41', 'Message Center'),
(17, 28, 749, '2024-12-30 07:07:10', 'Program Rating'),
(18, 6, 966, '2024-12-30 12:03:39', 'Search Programs'),
(19, 19, 273, '2024-03-07 00:55:06', 'Resource Downloads'),
(20, 20, 50, '2023-12-16 10:22:56', 'Course Evaluations');


-- studentAbroadProgram Bridge Inserts
INSERT INTO studentAbroadProgram (programID, sID) VALUES
(5, 1),
(8, 2),
(3, 3),
(7, 4),
(6, 5),
(27, 6),
(5, 7),
(1, 8),
(9, 9),
(6, 10),
(3, 11),
(7, 12),
(5, 13),
(2, 14),
(10, 15),
(8, 16),
(12, 17),
(6, 18),
(2, 19),
(20, 20),
(3, 21),
(5, 22),
(7, 23),
(10, 24),
(24, 25),
(8, 26),
(3, 27),
(9, 28),
(6, 29),
(2, 30),
(3, 1),
(6, 2),
(7, 3),
(5, 4),
(29, 5),
(16, 6),
(1, 7),
(4, 8),
(2, 9),
(8, 10),
(5, 11),
(8, 12),
(9, 13),
(6, 14),
(3, 15),
(2, 16),
(1, 17),
(10, 18),
(4, 19),
(8, 20),
(9, 21),
(7, 22),
(6, 23),
(3, 24),
(26, 25),
(5, 26),
(1, 27),
(7, 28),
(8, 29),
(4, 30),
(10, 1),
(7, 2),
(6, 3),
(8, 4),
(2, 5),
(5, 6),
(4, 7),
(9, 8),
(3, 9),
(10, 10),
(1, 11),
(2, 12),
(7, 13),
(5, 14),
(9, 15),
(6, 16),
(4, 17),
(3, 18),
(10, 19),
(1, 20),
(5, 21),
(6, 22),
(8, 23),
(9, 24),
(2, 25),
(4, 26),
(10, 27),
(3, 28),
(7, 29),
(5, 30),
(6, 1),
(2, 2),
(4, 3),
(1, 4),
(9, 5),
(10, 6),
(7, 7),
(3, 8),
(8, 9),
(5, 10),
(9, 31),
(9,32);



-- mentorshipMatch Data
INSERT INTO mentorshipMatch (matchID, menteeID, mentorID, dateMatched) VALUES
(1, 30, 1, '2024-09-08 22:55:29'),
(2, 30, 1, '2024-05-06 20:16:45'),
(3, 16, 2, '2024-03-12 11:09:16'),
(4, 16, 2, '2024-05-26 10:07:28'),
(5, 17, 3, '2024-03-09 09:28:33'),
(6, 17, 3, '2024-11-14 21:18:59'),
(7, 18, 4, '2024-02-14 23:33:03'),
(8, 18, 4, '2024-11-06 10:06:10'),
(9, 19, 5, '2024-07-21 18:42:56'),
(10, 19, 5, '2024-07-10 18:53:18'),
(11, 20, 6, '2024-02-16 09:29:34'),
(12, 20, 6, '2023-12-29 16:20:20'),
(13, 21, 7, '2024-09-23 09:51:46'),
(14, 21, 7, '2024-02-21 18:21:50'),
(15, 22, 8, '2024-03-10 08:47:31'),
(16, 22, 8, '2024-06-30 01:30:01'),
(17, 23, 9, '2024-09-06 03:22:33'),
(18, 23, 31, '2024-10-12 05:04:32'),
(19, 24, 10, '2024-05-09 23:22:26'),
(20, 24, 31, '2024-01-02 22:36:07'),
(21, 25, 11, '2024-10-16 05:58:43'),
(22, 25, 31, '2024-04-20 06:36:07'),
(23, 26, 12, '2024-04-11 00:20:35'),
(24, 26, 31, '2023-12-16 09:37:43'),
(25, 27, 13, '2024-09-18 21:12:21'),
(26, 27, 31, '2024-04-13 10:17:18'),
(27, 28, 14, '2024-03-23 04:01:03'),
(28, 28, 31, '2024-06-25 11:18:28'),
(29, 29, 15, '2024-11-12 17:42:34'),
(30, 29, 31, '2024-11-23 14:53:42'),
(31, 32, 31, '2024-11-23 14:53:42');


-- Major Data
INSERT INTO Major (majorID, majorName, Department) VALUES
(1, 'Computer Science', 'Engineering'),
(2, 'Mechanical Engineering', 'Engineering'),
(3, 'Psychology', 'Arts and Sciences'),
(4, 'Biology', 'Science'),
(5, 'Business Administration', 'Business'),
(6, 'Economics', 'Social Sciences'),
(7, 'Political Science', 'Social Sciences'),
(8, 'History', 'Arts and Humanities'),
(9, 'English Literature', 'Arts and Humanities'),
(10, 'Physics', 'Science'),
(11, 'Chemistry', 'Science'),
(12, 'Mathematics', 'Science'),
(13, 'Philosophy', 'Arts and Humanities'),
(14, 'Sociology', 'Social Sciences'),
(15, 'Anthropology', 'Social Sciences'),
(16, 'Electrical Engineering', 'Engineering'),
(17, 'Civil Engineering', 'Engineering'),
(18, 'Architecture', 'Design'),
(19, 'Art History', 'Arts and Humanities'),
(20, 'Music', 'Performing Arts'),
(21, 'Theater', 'Performing Arts'),
(22, 'Environmental Science', 'Science'),
(23, 'Nursing', 'Health Sciences'),
(24, 'Public Health', 'Health Sciences'),
(25, 'Communication', 'Social Sciences'),
(26, 'Journalism', 'Arts and Sciences'),
(27, 'Education', 'Education'),
(28, 'Linguistics', 'Arts and Humanities'),
(29, 'Computer Engineering', 'Engineering'),
(30, 'Chemical Engineering', 'Engineering');


-- studentMajor Bridge Inserts
INSERT INTO studentMajor (majorID, sID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20),
(21, 21),
(22, 22),
(23, 23),
(24, 24),
(25, 25),
(26, 26),
(27, 27),
(28, 28),
(29, 29),
(30, 30),
(1, 5),
(2, 7),
(3, 19),
(4, 3),
(5, 6),
(6, 12),
(7, 21),
(8, 2),
(9, 6),
(10, 3),
(11, 15),
(12, 21),
(13, 14),
(14, 13),
(15, 19),
(16, 20),
(17, 18),
(18, 21),
(19, 5),
(20, 9),
(21, 6),
(22, 12),
(23, 9),
(24, 5),
(25, 2),
(26, 27),
(27, 26),
(28, 19),
(29, 8),
(30, 6),
(1, 3),
(2, 5),
(3, 12),
(4, 6),
(5, 8),
(6, 19),
(7, 17),
(8, 10),
(9, 5),
(10, 21),
(11, 21),
(12, 23),
(13, 10),
(14, 19),
(15, 2),
(16, 7),
(17, 1),
(18, 14),
(19, 15),
(20, 6),
(21, 7),
(22, 16),
(23, 13),
(24, 9),
(25, 3),
(26, 8),
(27, 14),
(28, 11),
(29, 21),
(30, 18),
(5, 30),
(6, 5),
(7, 4),
(8, 3),
(9, 10),
(10, 6),
(11, 19),
(12, 2),
(13, 6),
(14, 6),
(15, 5),
(16, 6),
(17, 19);



-- Questions Data
INSERT INTO Question (qID, sID, content, datePosted, isApproved, abroadProgram) VALUES
(1, 16, 'What is the culture like in the city, and how can I best integrate into it?', '2024-03-06 03:34:04', 1, 1),
(2, 16, 'How do I open a bank account as an international student?', '2023-11-30 21:12:47', 1, 2),
(3, 17, 'Are there any cultural differences I should be aware of when studying here?', '2024-11-03 12:04:12', 1, 3),
(4, 17, 'Are there internship or job opportunities available for international students?', '2024-02-08 07:52:40', 1, 4),
(5, 18, 'What is the general attitude toward international students in this country?', '2024-02-16 02:36:42', 1, 5),
(6, 18, 'What is the culture like in the city, and how can I best integrate into it?', '2024-02-09 02:59:01', 1, 6),
(7, 19, 'Are there any local banks that offer student accounts with no fees?', '2024-01-26 04:05:28', 1, 7),
(8, 19, 'Is it easy to travel around the country during weekends or holidays?', '2024-01-01 14:21:17', 1, 8),
(9, 20, 'What are the most common challenges international students face in this city or country?', '2024-11-17 14:58:54', 1, 9),
(10, 20, 'How do I get a residence permit or extend my stay if I decide to stay longer?', '2024-04-17 12:29:47', 1, 10),
(11, 21, 'Can I work part-time while studying abroad?', '2024-04-26 21:55:13', 1, 11),
(12, 21, 'What is the culture like in the city, and how can I best integrate into it?', '2024-11-27 11:26:10', 1, 12),
(13, 22, 'Are there any local traditions or holidays I should be aware of during my stay?', '2024-06-04 20:22:01', 1, 13),
(14, 22, 'What is the local attitude toward environmental sustainability and eco-friendly practices?', '2023-12-13 04:18:44', 1, 14),
(15, 23, 'Can I transfer credits from my study abroad program back to my home institution?', '2023-12-23 13:15:54', 1, 15),
(16, 23, 'Are there any local networking or career events for international students?', '2024-06-24 02:24:28', 1, 16),
(17, 24, 'How do I get involved in research or academic opportunities as an international student?', '2024-07-15 18:19:40', 1, 17),
(18, 24, 'How can I stay connected with family and friends back home while abroad?', '2024-08-31 00:02:15', 1, 18),
(19, 25, 'Are there opportunities for international students to engage in local political or social movements?', '2024-08-29 18:03:12', 1, 19),
(20, 25, 'What are the main safety concerns in this city or country?', '2024-09-26 12:01:50', 1, 20),
(21, 26, 'What is the procedure for enrolling in courses as an international student?', '2024-08-19 23:52:13', 1, 21),
(22, 26, 'How safe is the neighborhood around the university for international students?', '2024-11-12 05:43:41', 1, 22),
(23, 32, 'Are there any local networking or career events for international students?', '2024-11-08 00:39:47', 1, 23),
(24, 32, 'What is the culture like in the city, and how can I best integrate into it?', '2024-11-09 18:55:52', 1, 24),
(25, 32, 'Are there scholarships available for international students?', '2023-12-14 15:45:50', 1, 25),
(26, 32, 'How can I stay updated on events and activities on campus?', '2024-07-20 00:42:18', 1, 26),
(27, 29, 'What color is the sky?', '2024-03-26 22:31:39', 0, 27),
(28, 29, 'Where can I find some lions?', '2024-09-08 11:25:42', 0, 28),
(29, 30, 'Who is the best professor in the world?', '2024-02-15 19:11:11', 0, 29),
(30, 30, 'Hello, hello, hello, hello, hello!', '2023-12-11 14:49:55', 0, 30);


-- Replies Data
INSERT INTO Reply (replyID, sID, qID, content, datePosted, isApproved) VALUES
(1, 1, 1, 'The city culture is vibrant and diverse—attend local events, explore community spaces, and connect with locals to integrate smoothly.', '2023-12-21 18:00:01', 1),
(2, 1, 2, 'To open a bank account, you will need your passport, visa, I-20/DS-2019, proof of address, and sometimes a Social Security number or ITIN.', '2024-04-14 03:54:34', 1),
(3, 2, 3, 'Yes, cultural norms like punctuality, individualism, and direct communication are common—observing and asking questions can help you adapt.', '2024-10-31 10:17:30', 1),
(4, 2, 4, 'Yes, international students can access internships or jobs through CPT, OPT, or on-campus roles—check your visa restrictions first.', '2024-06-11 06:49:42', 1),
(5, 3, 5, 'The general attitude is welcoming, with support networks in place, though experiences may vary depending on location and community.', '2024-06-30 07:13:39', 1),
(6, 3, 6, 'The city culture is vibrant and diverse—attend local events, explore community spaces, and connect with locals to integrate smoothly.', '2024-11-08 11:06:11', 1),
(7, 4, 7, 'Yes, local banks like Chase, Wells Fargo, and regional credit unions often offer no-fee student accounts—check specific terms.', '2024-07-15 01:30:55', 1),
(8, 4, 8, 'Yes, traveling is easy with extensive bus, train, and flight networks, plus budget-friendly options like carpooling or rideshares.', '2023-12-13 02:23:45', 1),
(9, 5, 9, 'Common challenges include adjusting to cultural differences, navigating visa restrictions, managing finances, and dealing with homesickness.', '2024-04-17 18:17:39', 1),
(10, 5, 10, 'To extend your stay, you can apply for a visa extension or a change of status through USCIS or the relevant immigration authority before your current permit expires.', '2024-11-11 00:00:02', 1),
(11, 6, 11, 'Yes, most international students can work part-time on-campus or through internships, depending on their visa type—check the specific work restrictions for your visa.', '2024-10-13 02:14:24', 1),
(12, 6, 12, 'The city culture is vibrant and diverse—attend local events, explore community spaces, and connect with locals to integrate smoothly.', '2023-12-19 13:01:29', 1),
(13, 7, 13, 'In Rome, you will encounter traditions like Ferragosto in August, celebrating summer with festivals, and the Feast of St. Peter and Paul in June—Italian holidays often involve family gatherings and local festivals.', '2023-12-25 16:42:47', 1),
(14, 7, 14, 'In Rome, there is growing support for sustainability, with many locals prioritizing recycling, sustainable transport, and green spaces, while eco-friendly initiatives continue to expand.', '2024-09-01 14:13:34', 1),
(15, 8, 15, 'Yes, most study abroad programs allow credit transfers, but you’ll need to get approval from Northeastern beforehand to ensure compatibility.', '2024-10-26 08:19:17', 1),
(16, 8, 16, 'Yes, many cities offer networking events, career fairs, and workshops for international students, typically organized by universities, embassies, and local organizations.', '2024-11-01 12:43:06', 1),
(17, 9, 17, 'You can get involved in research by connecting with professors, joining academic clubs, or applying for research assistant positions through your university or department.', '2024-08-24 06:41:20', 1),
(18, 9, 18, 'You can stay connected through regular video calls, messaging apps, and social media. Whatsapp was very helpful for me!', '2024-08-23 18:28:59', 1),
(19, 10, 19, 'International students can often engage in local political or social movements by joining student organizations, attending public events, or volunteering with local NGOs, provided they follow any visa-related restrictions.', '2024-03-08 04:08:47', 1),
(20, 10, 20, 'Main safety concerns may include petty theft, especially in tourist areas, traffic accidents, and natural disasters—staying aware of your surroundings and following local safety advice can help mitigate risks.', '2024-02-17 00:56:47', 1),
(21, 11, 21, 'To enroll in courses, international students typically need to register through the Northeastern online portal, meet with an academic advisor, and ensure compliance with visa requirements for full-time enrollment.', '2024-01-11 07:35:20', 1),
(22, 11, 22, 'The safety of a neighborhood varies, but most university areas are generally safe. It is recommended to stay informed about local conditions, follow safety tips, and avoid risky areas at night.', '2024-09-13 13:19:57', 1),
(23, 31, 23, 'Yes, many cities offer networking events, career fairs, and workshops for international students, typically organized by universities, embassies, and local organizations.', '2024-10-18 09:47:35', 1),
(24, 31, 24, 'The city culture is vibrant and diverse—attend local events, explore community spaces, and connect with locals to integrate smoothly.', '2024-04-05 06:01:09', 1),
(25, 31, 25, 'Yes, many universities and external organizations offer scholarships for international students, based on merit or need.', '2024-11-14 11:39:22', 1),
(26, 31, 26, 'You can stay updated on campus events by following university social media accounts, subscribing to newsletters, and regularly checking bulletin boards or online event calendars.', '2024-10-14 14:26:03', 1),
(27, 14, 27, 'BAD QUESTION!!!', '2024-08-04 04:31:53', 0),
(28, 14, 28, 'I have no idea.', '2024-01-02 15:48:21', 0),
(29, 15, 29, 'Yo Mama!', '2023-12-21 21:11:44', 0),
(30, 15, 30, 'PlEASE DO NOT BOTHER ME!', '2024-08-13 11:24:25', 0);


SELECT avg(locRating)
FROM Rating
WHERE programID = 2;

# ## Making the data entries
# INSERT INTO abroadProgram(programID, programName, prgmDescription, locationID, programType, empID)
# VALUES ( 00000000001, 'NUin.ROME', 'Embark on a transformative academic journey in the heart of Rome, Italy—a city where history, art, philosophy, and culture converge. The NUIN Rome program offers a curated selection of humanities courses designed to immerse students in the richness of Western civilization while fostering a deep appreciation for global perspectives.
# Through an interdisciplinary approach, students explore the historical, cultural, and philosophical dimensions of Rome as a living classroom. Courses are taught by distinguished faculty and emphasize critical thinking, analytical writing, and intercultural understanding. Students have the opportunity to engage directly with the city''s iconic landmarks, from the Colosseum to the Vatican, as part of their coursework, connecting theory to real-world experience.'
#        , 00000000001, 'NU.in', 00000000001),
#        ( 00000000002, 'Dialogue in London', 'Immerse yourself in the vibrant history and cutting-edge innovations of London, one of the world’s leading hubs for science, technology, and culture. This Dialogue of Civilizations program is designed for College of Science majors eager to explore the intersections of scientific discovery, societal impact, and cultural development.
# Students will delve into the history of science in the UK, from the groundbreaking contributions of figures like Newton and Darwin to modern advancements in fields such as medicine, environmental science, and artificial intelligence. Through interactive coursework, guest lectures from leading scientists, and visits to renowned institutions such as the Natural History Museum, the Science Museum, and the Francis Crick Institute, participants will gain a holistic understanding of how science shapes—and is shaped by—society.'
#        , 00000000002, 'Dialogue of Civilizations ', 00000000002);
#
# INSERT INTO Alerts (alertID, locationID, message)
# VALUES (00000000001, 00000000001, 'WARNING: High tempertures today. Keep hydrated and avoid the sun.'),
#        (00000000002, 00000000002, 'Classes are cancelled for the day due to poor weather.');
#
# INSERT INTO Resources (resourceID, locationID, category)
# VALUES (00000000001, 00000000001, 'Academics'),
#        (00000000002, 00000000002, 'Food & Restaurants');
#
# INSERT INTO Student(sID, fName, lName, email, blurb, role)
# VALUES (00000000101, 'Kristen', 'Bell', 'kristen.bell@gmail.com', 00000000002, 'Loves exploring new cities', 'mentee',
#         00000000001),
#        (00000000102, 'Jackie', 'Torres', 'jtorres@gmail.com', 00000000001, 'Passionate about international relations',
#         'mentee', 00000000002),
#        (00000000201, 'Leighton', 'Meester', 'leighmeester@gmail.com', 00000000002, 'Interested in behavioral economics',
#         'mentor', 00000000002),
#        (00000000202, 'Ed', 'Westwick', 'e.west@gmail.com', 00000000001, 'All things politics', 'mentor', 00000000002);
#
# INSERT INTO mentorshipMatch (matchID, menteeID, mentorID)
# VALUES (00000000001, 00000000101, 00000000201),
#        (00000000002, 00000000102, 00000000202);
#
# INSERT INTO Major (majorID, majorName, department)
# VALUES (00000000001, 'International Relations', 'Political Science'),
#        (00000000002, 'Economics', 'Humanities');
#
# INSERT INTO Location(locationID, city, country, description)
# VALUES (00000000001, 'Rome', 'Italy',
#         'Discover the heart of Western civilization in Rome, where ancient history, art, and culture come alive. Explore iconic landmarks like the Colosseum and Vatican City while delving into humanities courses that connect the city''s rich past to contemporary global issues.'),
#        (00000000002, 'London', 'United Kingdom',
#         'Immerse yourself in London, a global epicenter of science, technology, and culture. From the halls of the British Museum to cutting-edge research institutions, this program bridges the history of scientific discovery with its modern-day impact on society.');
#
# INSERT INTO Rating(programID, sID, locRating, profRating, avgRating, comment)
# VALUES (00000000001, 00000000001, 5, 4.5, 4.7,
#         'This was a fun program! Would have liked to see more professor and course in the historical environment.'),
#        (00000000002, 00000000002, 4, 4.5, 4.25,
#         'Dialogue in London was great! I loved seeing the clock tower and Princess Diana. Classes were very engaging, but weather was dreary.');
#
# INSERT INTO adminEmployee(empID, title, fName, lName, email, courseID)
# VALUES (00000000001, 'IT Administrator', 'Timothee', 'Chalamet', 'timmychal@gmail.com', 00000000001),
#        (00000000002, 'Global Advice Personnel', 'James', 'Bond', 'bond.james@gmail.com', 00000000002);
#
# INSERT INTO engagementAnalytics(featureID, empID, usageCount, feature)
# VALUES (00000000001, 00000000002, 3, 'Login'),
#        (00000000002, 00000000001, 8, 'Mentorship Forum');
#
# INSERT INTO Course(courseID, courseName, courseDescription, programID, professorID)
# VALUES (00000000001, 'Introduction to Databases',
#         'Data is everywhere!  This course will introduce you to relational database management systems (RDBMS).  We will study the foundations of the relational model, design of a relational database, SQL, use of a modern RDBMS, and more advanced topics as time permits. Prerequisites for this course are CS2500 or DS 2000 or EECE 2560.',
#         00000000001, 00000000001),
#        (00000000002, 'Intro to London Architecture',
#         'This course introduces students to the history of Britain and its interaction with the world. The course follows British history from the Roman Empire to the present-day. The aim is to examine Britain’s relationships with other countries and cultures, exploring social, economic, and cultural developments, as well as political and diplomatic ones. As well as understanding these developments discretely, students will also be encouraged to see how they affect one another.',
#         00000000002, 00000000002);
#
# INSERT INTO Professor(profID, fName, lName, department, email)
# VALUES (00000000001, 'Mark', 'Fontenot', 'Computer Science', 'fontenot.m@northeastern.edu'),
#        (00000000002, 'Harry', 'Potter', 'History', 'potter.h@hogwarts.edu');
#
# INSERT INTO Reply(replyID, sID, qID, content, datePosted, isApproved)
# VALUES (00000000001, 00000000001, 00000000001,
#         'The food was so delicious and the people were so kind. Definitely get a good pair of sneakers because you will be doing a lot of walking.',
#         DEFAULT, 1),
#        (00000000002, 00000000002, 00000000002, 'The professor was such an idiot!!', DEFAULT, 0);
#
# INSERT INTO Question(qID, sID, content, datePosted, isApproved)
# VALUES (00000000001, 00000000001, 'What is Rome like?', DEFAULT, 1),
#        (00000000002, 00000000002, 'Poopoo Peepee!!!', DEFAULT, 0);
#
# INSERT INTO studentAbroadProgram (programID, sID)
# VALUES (00000000001, 00000000001),
#        (00000000002, 00000000002);
#
# INSERT INTO employeeAbroadProgram (programID, empID)
# VALUES (00000000001, 00000000001),
#        (00000000002, 00000000002);
#
# INSERT INTO studentMajor (majorID, sID)
# VALUES (00000000001, 00000000001),
#        (00000000002, 00000000002);
#
# --------------- PERSONA 1
# ---------------
#
# -- 1.1: Creating a reply
# INSERT INTO Reply (replyID, sID, qID, isApproved)
# VALUES (00000000003, 00000000456, 00000000123, FALSE);
#
# -- 1.2: Creating ratings
# INSERT INTO Rating (ratingID, programID, sID, locRating, profRating, avgRating, comment)
# VALUES (DEFAULT, 00000000001, 00000000456, 5, 4, 4.5, 'Great program and location!');
#
# -- 1.3: Reading/selecting the location that the student studied abroad at
# SELECT sap.programID, ap.programName, ap.prgmDescription, loc.city, loc.country
# FROM studentAbroadProgram sap
#          JOIN abroadProgram ap
#               ON sap.programID = ap.programID
#          JOIN Location loc
#               ON ap.locationID = loc.locationID
# WHERE sap.sID = 00000000456;
#
# -- 1.4: Updating the blurb
# UPDATE Student
# SET blurb = 'I’ve added more experience since my time in Rome!'
# WHERE sID = 00000000456;
#
# -- 1.5: Reading/filtering potential mentees by specific majors
# SELECT s.sID, s.fName, s.lName, m.majorName, sap.programID
# FROM Student s
#          JOIN studentMajor sm
#               ON s.sID = sm.sID
#          JOIN Major m
#               ON sm.majorID = m.majorID
#          JOIN studentAbroadProgram sap
#               ON s.sID = sap.sID
# WHERE m.majorName = 'Business'
#   AND sap.programID = 00000000001;
#
# -- 1.6: Creating and Deleting mentorship match pai
# INSERT INTO mentorshipMatch (matchID, menteeID, mentorID)
# VALUES (DEFAULT, 00000000789, 00000000456);
#
# DELETE
# FROM mentorshipMatch
# WHERE matchID = 00000000001
#   AND mentorID = 00000000456;
#
# --------------- PERSONA 2
# ---------------
#
# -- 2.1: ask a question about future global experience
# INSERT INTO Question(qID, sID, content, isApproved)
# VALUES (00000000003, 00000000101, 'What should I pack for a semester in Rome?', 1);
#
# SELECT *
# From Question
# WHERE sID = 00000000101;
#
# UPDATE Question
# SET isApproved = 1
# WHERE qID = 00000000003;
#
# DELETE
# FROM Question
# where qID = 00000000003;
#
# -- 2.2: search for location based on my major
# SELECT l.locationID, l.city, l.country, ap.programName, ap.prgmDescription
# FROM Location l
#          JOIN abroadProgram ap ON l.locationID = ap.locationID
#          JOIN Major m ON m.majorID = 00000000002
# ORDER BY l.city;
#
# -- 2.3: question the global experience office
# INSERT INTO Question (qID, sID, content, datePosted, isApproved)
# VALUES (00000000003, 00000000202, 'Do I get to choose my roommate?', DEFAULT, 1);
#
# -- 2.4: view  the replies to a question
# SELECT q.content, r.replyID, r.sID, r.qID, r.datePosted, r.isApproved
# FROM Question q
#          JOIN Reply r ON q.qID = r.qID
# WHERE q.qID = 00000000001;
#
# -- 2.5: view rating on specific locations
# SELECT l.city,
#        l.country,
#        p.fName,
#        p.lName,
#        r.locRating,
#        r.profRating,
#        r.avgRating,
#        r.comment
# FROM Rating r
#          JOIN Location l ON r.locRating = l.locationID
#          JOIN Professor p ON r.profRating = p.profID
# WHERE r.sID = 00000000303;
#
# -- 2.6: find another student going to the same location
# SELECT s.fName, s.lName, s.email, p.programName, l.city, l.country
# FROM Student s
#          JOIN studentAbroadProgram sap ON s.sID = sap.sID
#          JOIN abroadProgram p ON sap.programID = p.programID
#          JOIN Location l ON p.locationID = l.locationID
# WHERE l.locationID = 00000000001
#   AND s.sID != 00000000101
# ORDER BY s.fName, s.lName;
#
# --------------- PERSONA 3
# ---------------
#
# -- 3.1: Deleting/limiting comments
# DELETE
# FROM Reply
# WHERE isApproved = 0;
#
# -- 3.2: Maintaining locations
# INSERT INTO Location(locationID, city, country, description)
# VALUES (3, 'Bangkok', 'Thailand', 'Bangkok, the vibrant capital of Thailand, is a bustling metropolis known for its ornate temples, lively street markets, and dynamic nightlife. The city blends traditional culture with modernity, offering a mix of historic sites, shopping districts, and world-class dining experiences.');
#
# -- 3.3: Moderate a rating system for courses & professors
# SELECT *
# FROM Rating
# WHERE profRating = 4;
#
# -- 3.4: Moderate a rating system for accomodations and lifestyle
# UPDATE Rating
# SET locRating = 3,
#     comment   = 'Great environment for keeping up with athletic habits. May not be suitable for those not accustomed to routine physical activity.'
# WHERE ratingID = 00000000001;
#
# -- 3.5: Moderate a rating system for location
# DELETE
# FROM Rating
# WHERE ratingID = 00000000002;
#
# -- 3.6: Creating/maintaining forum posts
# UPDATE Reply
# SET content = 'Updated reply content here.'
# WHERE replyID = 00000000001;
#
# --------------- PERSONA 4
# ---------------
#
# -- 4.1: update resources for specific loc
# UPDATE Resources
# SET category = 'Updated Housing Information'
# WHERE locationID = 1;
#
# -- 4.2: retrieve real-time feedback on housing, professors, and local services
# -- in order of most recent to least recent
# SELECT locRating, profRating, comment, datePosted
# FROM Rating
# WHERE programID = 1
# ORDER BY datePosted DESC;
#
# -- 4.3: track app usage over monthly periods
# SELECT empID, featureID, usageCount, DATE_FORMAT(date, '%Y-%m'), feature AS usageMonth
# FROM engagementAnalytics
# WHERE date >= '2023-11-18'
# GROUP BY empID, featureID, usageMonth, feature
# ORDER BY usageMonth DESC;
#
# -- 4.4: moderate alerts
# INSERT INTO Alerts(alertID, locationID, message)
# VALUES (5, 1, 'Record high temperatures today, stay hydrated!');
#
# -- 4.5: moderate students
# INSERT INTO Student(sID, fName, lName, email, majorID, blurb, role, programID)
# VALUES (5, 'Melody', 'Green', 'melodygreen@gmail.com', 2,
#         'Hi! Im a second year student who just returned from Rome and want to be your mentor!',
#         'mentor', 1);
#
# -- 4.6: control resources
# DELETE
# FROM Resources
# WHERE resourceID = 2;
# CREATE TABLE IF NOT EXISTS abroadProgram
# (
#     programID       INT(11) UNIQUE PRIMARY KEY,
#     programName     VARCHAR(100)   NOT NULL,
#     prgmDescription LONGTEXT       NOT Null,
#     locationID      INT(11) UNIQUE NOT NULL,
#     programType     VARCHAR(100)   NOT NULL,
#     empID           INT(11) UNIQUE NOT NULL,
#     CONSTRAINT ap_fk_01 FOREIGN KEY (programID)
#         REFERENCES employeeAbroadProgram (programID)
#
# );