CREATE TABLE Borrower (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL,
	Surname TEXT NOT NULL,
	Contact TEXT NOT NULL
);

CREATE TABLE Publisher (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL
);

CREATE TABLE Book (
	ID INTEGER PRIMARY KEY,
	Title TEXT NOT NULL,
	PublisherID INTEGER,
	Damaged INTEGER NOT NULL,
	FOREIGN KEY (PublisherID) REFERENCES Publisher (ID)
);

CREATE TABLE Loan (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	BorrowerID INTEGER,
	BookID INTEGER,
	DateBorrowed TEXT,
	FOREIGN KEY (BorrowerID) REFERENCES Borrower(ID),
	FOREIGN KEY (BookID) REFERENCES Book(ID)
);