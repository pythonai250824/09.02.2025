CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    course_avg_grade NUMERIC DEFAULT 0
);

CREATE TABLE grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
    course_name VARCHAR(100) NOT NULL,
    grade NUMERIC NOT NULL CHECK (grade >= 0 AND grade <= 100)
);

CREATE OR REPLACE FUNCTION update_avg_grade()
RETURNS TRIGGER AS $$
BEGIN
    -- Calculate the average grade for the student
    UPDATE students
    SET course_avg_grade = (
        SELECT AVG(grade)
        FROM grades
        WHERE grades.student_id = NEW.student_id
    )
    WHERE student_id = NEW.student_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_insert_grade
AFTER INSERT ON grades
FOR EACH ROW
EXECUTE FUNCTION update_avg_grade();

INSERT INTO students (name) VALUES ('Alice');
INSERT INTO students (name) VALUES ('Bob');

INSERT INTO grades (student_id, course_name, grade) VALUES (1, 'Math', 85);
INSERT INTO grades (student_id, course_name, grade) VALUES (1, 'Science', 90);
INSERT INTO grades (student_id, course_name, grade) VALUES (2, 'Math', 78);
INSERT INTO grades (student_id, course_name, grade) VALUES (2, 'Science', 88);
