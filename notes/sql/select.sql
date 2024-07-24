SELECT * from Book WHERE PublisherID IS NOT NULL;
SELECT Name from Publisher;
SELECT Title FROM Book WHERE PublisherID=4 AND Damaged=0;
SELECT Title FROM Book WHERE PublisherID=1 OR PublisherID=2;
SELECT * from Loan WHERE DateBorrowed > "20180101";
SELECT * from Loan ORDER BY BookID;
SELECT * FROM Loan WHERE BorrowerID=3 ORDER BY BookID DESC;
SELECT count(id) from loan;

/* use group by with aggregate functions */
SELECT count(borrowerid), Borrower.FirstName, Borrower.Surname
FROM loan, borrower
WHERE loan.BorrowerID = Borrower.ID
GROUP BY borrower.ID
ORDER BY Borrower.FirstName;

SELECT Book.ID, Book.Title, Publisher.Name
FROM Book
LEFT OUTER JOIN Publisher
ON Book.PublisherID = Publisher.ID
WHERE Book.Damaged = 0;

/* have to use left outer join becasue not all borrowers have loans */
SELECT Loan.BorrowerID, Borrower.FirstName, Borrower.Surname, Count(Loan.BookID)
FROM Borrower
LEFT OUTER JOIN Loan
ON Borrower.ID = Loan.BorrowerID
GROUP BY Borrower.ID
ORDER BY Borrower.ID DESC;
