import sqlite3

def search_student():

    name = input("Enter student name: ")

    conn = sqlite3.connect("database/students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name=?",
        (name,)
    )

    student = cursor.fetchone()

    if student:
        print(student)

    else:
        print("Student Not Found")

    conn.close()