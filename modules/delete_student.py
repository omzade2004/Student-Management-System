import sqlite3

def delete_student():

    student_id = int(input("Enter student ID: "))

    conn = sqlite3.connect("database/students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    print("Student Deleted Successfully")