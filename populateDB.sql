USE aliens;
INSERT INTO Alien (name, email) VALUES ("zorb", "zorber@zorbsplace.net");
INSERT INTO Alien (name, email) VALUES ("shleem", "shleem@zorbsplace.net");
INSERT INTO Expedition (sightingId, craftModel, duration) VALUES (84926, "Shlorbian", 20);
INSERT INTO AlienToExpedition VALUES (1, 207);
INSERT INTO AlienToExpedition VALUES (2, 207);
ALTER TABLE governmentemployee
ADD COLUMN user_id INT,
ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES auth_user(id);
#SELECT * FROM GovernmentEmployee;
#SELECT * FROM expedition;
INSERT INTO GovernmentNote (sightingId, employeeId, text, date) VALUES (1, 1, "This was us", "2004-09-09");