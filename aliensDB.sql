DROP DATABASE IF EXISTS aliens;
CREATE DATABASE aliens;
USE aliens;
GRANT ALL privileges on aliens.* TO 'django'@'localhost' WITH grant option;
#SELECT * FROM auth_user_user_permissions;
#DELETE FROM auth_user;
#SELECT COUNT(sightingId) FROM sighting;#86019
#SELECT s.sightingId, s.date, s.comments, s.city, s.state, s.shape, s.country, s.duration, s.dateposted, s.longitude, s.latitude, AVG(c.believability) as average, SUM(c.believability) as sum FROM sighting as s LEFT JOIN comment as c ON s.sightingId = c.sightingId GROUP BY s.sightingId ORDER BY sum DESC LIMIT 10;
#SELECT a.alienId, name FROM alien as a LEFT JOIN alientoexpedition as ae ON a.alienId = ae.alienId LEFT JOIN expedition as e ON ae.expeditionId = e.expeditionId WHERE sightingId = 84926;
#SELECT a.alienId, name, COUNT(ae.expeditionId) as spotted FROM alien as a LEFT JOIN alientoexpedition as ae ON a.alienId = ae.alienId LEFT JOIN expedition as e ON ae.expeditionId = e.expeditionId GROUP BY a.alienId, a.name;
SELECT n.noteid, name, country, position, text FROM governmentnote as n LEFT JOIN governmentemployee as e ON n.employeeId = e.employeeId WHERE n.sightingId = 1;
#SELECT * FROM alientoexpedition;
#SELECT s.sightingId, s.date, s.comments, s.city, s.state, s.shape, s.country, s.duration, s.dateposted, s.longitude, s.latitude, SUM(c.believability) as sum, AVG(c.believability) as average FROM sighting as s LEFT JOIN comment as c ON s.sightingId = c.sightingId WHERE latitude <= 1 and latitude >= -90 and longitude <= 90 and longitude >= -90 GROUP BY s.sightingId ORDER BY sum DESC;
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
    comments VARCHAR(15000),
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
