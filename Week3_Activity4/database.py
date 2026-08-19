import sqlite3
import dummy_data

def create_connection():
    conn = sqlite3.connect("Week3_Activity4/activity4.db")
    return conn

def create_tables():
    # Open and read the schema file for DB
    with open("Week3_Activity4/scema.sql", "r") as schema:
        sql_script = schema.read()

    # Execute the script
    conn = create_connection()
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.close()
    print("Database schema loaded and tables created")
    
def populate_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert dummy data into the tables
    cursor.executemany("INSERT OR IGNORE INTO Student VALUES (?, ?, ?, ?)", dummy_data.STUDENTS)
    cursor.executemany("INSERT OR IGNORE INTO Lecturer VALUES (?, ?, ?, ?, ?)", dummy_data.LECTURERS)
    cursor.executemany("INSERT OR IGNORE INTO Subjects VALUES (?, ?, ?)", dummy_data.SUBJECTS)
    cursor.executemany("INSERT OR IGNORE INTO Lecture VALUES (?, ?, ?, ?, ?)", dummy_data.LECTURES)
    cursor.executemany("INSERT OR IGNORE INTO Lectures VALUES (?, ?, ?)", dummy_data.LECTURES_RELATIONS)
    cursor.executemany("INSERT OR IGNORE INTO Enrollment VALUES (?, ?, ?, ?)", dummy_data.ENROLLMENTS)
    cursor.executemany("INSERT OR IGNORE INTO Enrolls VALUES (?, ?, ?)", dummy_data.ENROLLS_RELATIONS)

    conn.commit()
    conn.close()
    print("Database populated")
