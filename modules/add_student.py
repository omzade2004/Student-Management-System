import sqlite3
from modules.grade_system import calculate_grade

def add_student():

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    grade = calculate_grade(marks)

    conn = sqlite3.connect("database/students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, marks, grade) VALUES(?,?,?)",
        (name, marks, grade)
    )

    conn.commit()
    conn.close()

    print("Student Added Successfully")