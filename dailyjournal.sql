CREATE TABLE 'MOODS' (
    'id'    INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT
    'label' TEXT NOT NULL
)

CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
	`mood_id`	TEXT NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);





INSERT INTO `Moods` VALUES (null, "Focused");
INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Frustrated");

INSERT INTO `Entries` VALUES (null, "2020-07-22T11:50", "eventHubs", "what are eventHub?", 1);
INSERT INTO `Entries` VALUES (null, "2020-07-23T11:43", "comments", "how do you comment?", 2);
INSERT INTO `Entries` VALUES (null, "2020-07-23T21:54", "Javascript", "I dont know man", 3);

SELECT * FROM Entries