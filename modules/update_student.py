import sqlite3
from modules.grade_system import calculate_grade

def update_student():

    student_id = int(input("Enter student ID: "))
    new_marks = int(input("Enter new marks: "))

    new_grade = calculate_grade(new_marks)

    conn = sqlite3.connect("database/students.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks=?, grade=? WHERE id=?",
        (new_marks, new_grade, student_id)
    )

    conn.commit()
    conn.close()

    print("Student Updated Successfully")