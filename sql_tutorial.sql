CREATE TABLE student (
    student_id INT,
    name VARCHAR(20),
    major VARCHAR(20)
    PRIMARY KEY(student_id)
);
SELECT * FROM student;

INSERT INTO student VALUES(1, 'Jack', 'Biology');