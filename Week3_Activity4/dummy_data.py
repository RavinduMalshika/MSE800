STUDENTS = [
    (1001, 'Alice', 'Smith', '2001-05-14'),
    (1002, 'Bob', 'Jones', '2000-11-22'),
    (1003, 'Charlie', 'Brown', '2002-01-10'),
    (1004, 'Diana', 'Prince', '1999-08-30'),
    (1005, 'Evan', 'Wright', '2001-03-18')
]

LECTURERS = [
    (501, 'Miller', 'Alan', 'a.miller@univ.edu', '123 University Ave'),
    (502, 'Davis', 'Sarah', 's.davis@univ.edu', '456 Campus Drive')
]

SUBJECTS = [
    ('CS101', 3, 'Introduction to Computer Science'),
    ('DB201', 4, 'Database Systems & SQL'),
    ('MATH11', 3, 'Discrete Mathematics')
]

LECTURES = [
    ('CC_CS101_A', 'Computer Science', '09:00 AM', '2026-09-01', 'Intro to CS - Sec A'),
    ('CC_DB201_A', 'Databases', '11:00 AM', '2026-09-01', 'Database Systems - Sec A'),
    ('CC_MATH11_A', 'Mathematics', '02:00 PM', '2026-09-02', 'Discrete Math - Sec A')
]

LECTURES_RELATIONS = [
    (501, 'CS101', 'CC_CS101_A'),   
    (501, 'DB201', 'CC_DB201_A'),  
    (502, 'MATH11', 'CC_MATH11_A')  
]

ENROLLMENTS = [
    ('ENR_1001', '2026-08-15', 'Computer Science', 'CC_CS101_A'),
    ('ENR_1002', '2026-08-15', 'Computer Science', 'CC_CS101_A'),
    ('ENR_1003', '2026-08-16', 'Database Systems', 'CC_DB201_A'),
    ('ENR_1004', '2026-08-16', 'Database Systems', 'CC_DB201_A'),
    ('ENR_1005', '2026-08-17', 'Mathematics', 'CC_MATH11_A'),
    ('ENR_1006', '2026-08-18', 'Mathematics', 'CC_MATH11_A'),
    ('ENR_1007', '2026-08-18', 'Mathematics', 'CC_MATH11_A'),
    ('ENR_1007', '2026-08-18', 'Database Systems', 'CC_DB201_A')
]

ENROLLS_RELATIONS = [
    (1001, 'ENR_1001', 'CC_CS101_A'),
    (1001, 'ENR_1001', 'CC_CS101_A'),
    (1002, 'ENR_1002', 'CC_CS101_A'),
    (1003, 'ENR_1003', 'CC_DB201_A'),
    (1004, 'ENR_1004', 'CC_DB201_A'),
    (1005, 'ENR_1005', 'CC_MATH11_A'),
    (1001, 'ENR_1006', 'CC_MATH11_A'),
    (1003, 'ENR_1007', 'CC_MATH11_A'),
    (1001, 'ENR_1008', 'CC_DB201_A'),
]
