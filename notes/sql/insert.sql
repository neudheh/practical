INSERT INTO Borrower (FirstName, Surname, Contact) VALUES ("Peter", "Tan", "99299345");
INSERT INTO Borrower (FirstName, Surname, Contact) VALUES ("Sarah", "Lee", "81111123");
INSERT INTO Borrower (FirstName, Surname, Contact) VALUES ("Kumara", "Ravi", "94456677");
INSERT INTO Borrower (FirstName, Surname, Contact) VALUES ("Some", "User", "11111111");

INSERT INTO Publisher (ID, Name) VALUES (1, "NPH");
INSERT INTO Publisher (ID, Name) VALUES (2, "Unpop");
INSERT INTO Publisher (ID, Name) VALUES (3, "Appleson");
INSERT INTO Publisher (ID, Name) VALUES (4, "Squirrel");
INSERT INTO Publisher (ID, Name) VALUES (5, "Yellow Flame");

INSERT INTO Book (ID, Title, PublisherID, Damaged) VALUES (1, "The Lone Gatsby", 5, 0);
INSERT INTO Book (ID, Title, PublisherID, Damaged) VALUES (2, "A Winter's Slumber", 4, 1);
INSERT INTO Book (ID, Title, PublisherID, Damaged) VALUES (3, "Life of Pie", 4, 0);
INSERT INTO Book (ID, Title, PublisherID, Damaged) VALUES (4, "A Brief History Of Primates", 3, 0);
INSERT INTO Book (ID, Title, PublisherID, Damaged) VALUES (5, "To Praise a Mocking Bird", 2, 0);
INSERT INTO Book (ID, Title, PublisherID, Damaged) VALUES (6, "The Catcher in the Eye", 1, 1);
INSERT INTO Book (ID, Title, Damaged) VALUES (123, "H2 Computing Ten Year Series", 0);

INSERT INTO Loan (ID, BorrowerID, BookID, DateBorrowed) VALUES (1, 3, 2, "20180220");
INSERT INTO Loan (ID, BorrowerID, BookID, DateBorrowed) VALUES (2, 3, 1, "20171215");
INSERT INTO Loan (ID, BorrowerID, BookID, DateBorrowed) VALUES (3, 2, 3, "20171231");
INSERT INTO Loan (ID, BorrowerID, BookID, DateBorrowed) VALUES (4, 1, 5, "20180111");