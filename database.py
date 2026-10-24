import sqlite3
def create_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
             student_id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL UNIQUE,
             gpa REAL NOT NULL CHECK (gpa >= 0 AND gpa <= 10)
        )
     """)
    connection.commit()
    connection.close()
    print("Database and table created successfully!")
def add_students(student_id, name, email, gpa):
    name = name.strip()
    email = email.strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return
    if not email or "@" not in email:
        print("Error: Enter a valid email address.")
        return
    try:
        gpa = float(gpa)
    except (ValueError, TypeError):
        print("Error: GPA must be a number.")
        return
    if not 0 <= gpa <= 10:
        print("Error: GPA must be between 0 and 10.")
        return
    connection = sqlite3.connect("students.db")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO students (student_id, name, email, gpa)
        VALUES (?, ?, ?, ?)
    """, (student_id, name, email, gpa))
        connection.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Error: student ID or email already exists.")
    finally:
        connection.close()
def view_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if records:
        print("\n--- student Records ---")
        for student in records:
            print(student)
    else:
        print("No student records found.")
    connection.close()
def search_student(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()  
    if student:
        print("Student found:", student)
    else:
        print("No student found")
    connection.close()
def update_student(student_id, new_name, new_email, new_gpa):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE students
        SET name = ?, email = ?, gpa = ?
        WHERE student_id = ?
       """, (new_name, new_email, new_gpa, student_id) )
    connection.commit()
    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student ID not found.")
        connection.close()
def delete_student(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student ID not found.")
        connection.close()
if __name__ == "__main__":
    create_database()
    add_students(1, "jon", "jon@gmail.com", 9.0)
    add_students(2, "ammu", "ammu@gmail.com", 8.0)
    add_students(3, "honey", "honey@gmail.com", 8.0)
    add_students(4, "anii", "anii@gmail.com", 8.7)
    view_students()
    search_student(2)
    update_student(2, "ammu", "ammu@gmail.com", 8.0)
    delete_student(2)

