-- Create a new database named UniversityDB
CREATE DATABASE UniversityDB;
USE UniversityDB;

-- Create a table named Students with specified attributes
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Major VARCHAR(50)
);

-- Insert 5 sample records into the Students table
INSERT INTO Students (StudentID, FirstName, LastName, Age, Major) VALUES
(1, 'John', 'Doe', 20, 'Computer Science'),
(2, 'Jane', 'Doe', 22, 'Electrical Engineering'),
(3, 'Mike', 'Smith', 21, 'Mathematics'),
(4, 'Sarah', 'Brown', 19, 'Physics'),
(5, 'Emily', 'Jones', 23, 'Chemistry');

-- Add a new column named GPA to the Students table
ALTER TABLE Students ADD COLUMN GPA DECIMAL(3,2);

-- Update the table to insert GPA values for each student
UPDATE Students SET GPA = 3.5 WHERE StudentID = 1;
UPDATE Students SET GPA = 3.7 WHERE StudentID = 2;
UPDATE Students SET GPA = 3.2 WHERE StudentID = 3;
UPDATE Students SET GPA = 3.9 WHERE StudentID = 4;
UPDATE Students SET GPA = 3.6 WHERE StudentID = 5;

-- Rename the Students table to EnrolledStudents
RENAME TABLE Students TO EnrolledStudents;

-- Create a table named Courses with specified attributes
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Instructor VARCHAR(100),
    Credits INT
);

-- Insert 3 sample records into the Courses table
INSERT INTO Courses (CourseID, CourseName, Instructor, Credits) VALUES
(101, 'Introduction to Computer Science', 'Dr. Alice Smith', 4),
(102, 'Linear Algebra', 'Dr. Bob Jones', 3),
(103, 'Modern Physics', 'Dr. Carol White', 4);

-- Drop the EnrolledStudents table from the database
DROP TABLE EnrolledStudents;
