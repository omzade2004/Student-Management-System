import sqlite3

def view_students():

    conn = sqlite3.connect("database/students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if not students:
        print("No Records Found")

    else:
        print("\n===== Student Records =====")

        for student in students:
            print(student)

    conn.close()