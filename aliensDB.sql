DROP DATABASE IF EXISTS aliens;
CREATE DATABASE aliens;
USE aliens;
GRANT ALL privileges on aliens.* TO 'django'@'localhost' WITH grant option;
#SELECT * FROM auth_user_user_permissions;
#DELETE FROM auth_user;
#SELECT COUNT(sightingId) FROM sighting;#86019
CREATE TABLE User (
	userId INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(35),
    email VARCHAR(35),
    dateJoined DATETIME
);
INSERT INTO User (name, email) VALUES ("Jeff", "jeff@jeff.com");

CREATE TABLE Sighting (
	sightingId INTEGER PRIMARY KEY AUTO_INCREMENT,
    userId INTEGER NOT NULL,
    date datetime,
    comments VARCHAR(1500),
    city VARCHAR(100),
    state VARCHAR(25),
    shape VARCHAR(25),
    country VARCHAR(255),
    duration INTEGER,
    datePosted DATETIME,
    longitude FLOAT,
    latitude FLOAT,
    FOREIGN KEY (userId) REFERENCES User(userId)
);

SELECT * FROM sighting;

CREATE TABLE Comment (
	commentId INTEGER PRIMARY KEY AUTO_INCREMENT,
    sightingId INTEGER NOT NULL,
    text VARCHAR(1500),
    date datetime,
    believability INTEGER,
    FOREIGN KEY (sightingId) REFERENCES Sighting(sightingId)
);

CREATE TABLE GovernmentEmployee (
	employeeId INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(35),
    country VARCHAR(25),
    position VARCHAR(35)
);
ALTER TABLE governmentemployee
ADD COLUMN user_id INT,
ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES auth_user(id);
SELECT * FROM GovernmentEmployee;

CREATE TABLE GovernmentNote (
	noteId INTEGER PRIMARY KEY AUTO_INCREMENT,
    sightingId INTEGER NOT NULL,
    employeeId INTEGER NOT NULL,
    text VARCHAR(500),
    date datetime,
    FOREIGN KEY (sightingId) REFERENCES Sighting(sightingId),
    FOREIGN KEY (employeeId) REFERENCES GovernmentEmployee(employeeId)
);

CREATE TABLE Expedition (
	expeditionId INTEGER PRIMARY KEY AUTO_INCREMENT,
    sightingId INTEGER NOT NULL,
    craftModel VARCHAR(35),
    duration INTEGER,
    FOREIGN KEY (sightingId) REFERENCES Sighting(sightingId)
);

select * from expedition;

CREATE TABLE Alien (
	alienId INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(35) NOT NULL,
    email VARCHAR(25) NOT NULL
);

CREATE TABLE AlienToExpedition (
	alienId INTEGER AUTO_INCREMENT,
    expeditionId INTEGER,
    PRIMARY KEY(alienId, expeditionId),
    FOREIGN KEY (alienId) REFERENCES Alien(alienId),
    FOREIGN KEY (expeditionId) REFERENCES Expedition(expeditionId)
);
