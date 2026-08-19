from database import create_connection

def get_all_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_student_count_in_each_course():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            sub.Subject_code,
            sub.Subject_udsc,
            COUNT(DISTINCT e.NID) AS Total_Students
        FROM Subjects sub
        LEFT JOIN Lectures lec ON sub.Subject_code = lec.Subject_code
        LEFT JOIN Enrolls e ON lec.CC_num = e.CC_num
        GROUP BY sub.Subject_code, sub.Subject_udsc;
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_students_enrolled_in_multiple_course():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            s.NID,
            s.F_name,
            s.L_name,
            COUNT(DISTINCT e.CC_num) AS Courses_Enrolled
        FROM Student s
        JOIN Enrolls e ON s.NID = e.NID
        GROUP BY s.NID, s.F_name, s.L_name
        HAVING COUNT(DISTINCT e.CC_num) > 1;
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows
