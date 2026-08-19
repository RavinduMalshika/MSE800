CREATE TABLE IF NOT EXISTS Student (
    NID INTEGER PRIMARY KEY,
    F_name TEXT NOT NULL,
    L_name TEXT NOT NULL,
    B_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Lecturer (
    Lecture_id INTEGER PRIMARY KEY,
    L_lastname TEXT NOT NULL,
    L_firstname TEXT NOT NULL,
    L_email TEXT NOT NULL,
    L_address TEXT
);

CREATE TABLE IF NOT EXISTS Subjects (
    Subject_code TEXT PRIMARY KEY,
    Subject_unit INTEGER,
    Subject_udsc TEXT
);

CREATE TABLE IF NOT EXISTS Lecture (
    CC_num TEXT PRIMARY KEY,
    Subject TEXT,
    Time TEXT,
    Date DATE,
    Lecture_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Enrollment (
    Student_code TEXT PRIMARY KEY,
    Date_of_enrolment DATE NOT NULL,
    Course_name TEXT NOT NULL,
    CC_num TEXT,
    FOREIGN KEY (CC_num) REFERENCES Lecture(CC_num)
);

CREATE TABLE IF NOT EXISTS Enrolls (
    NID INTEGER,
    Student_code TEXT,
    CC_num TEXT,
    PRIMARY KEY (NID, Student_code, CC_num),
    FOREIGN KEY (NID) REFERENCES Student(NID),
    FOREIGN KEY (Student_code) REFERENCES Enrollment(Student_code),
    FOREIGN KEY (CC_num) REFERENCES Lecture(CC_num)
);

CREATE TABLE IF NOT EXISTS Lectures (
    Lecture_id INTEGER,
    Subject_code TEXT,
    CC_num TEXT,
    PRIMARY KEY (Lecture_id, Subject_code, CC_num),
    FOREIGN KEY (Lecture_id) REFERENCES Lecturer(Lecture_id),
    FOREIGN KEY (Subject_code) REFERENCES Subjects(Subject_code),
    FOREIGN KEY (CC_num) REFERENCES Lecture(CC_num)
);
