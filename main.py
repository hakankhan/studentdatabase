import psycopg2
from prettytable import PrettyTable

# update the following lines
conn = psycopg2.connect(
    database="YOUR_DATABASE",
    user="YOUR_USER",
    host="localhost",
    password="YOUR_PASSWORD",
)
conn.autocommit = True
cur = conn.cursor()


def getAllStudents():
    table = PrettyTable()
    table.field_names = [
        "student_id",
        "first_name",
        "last_name",
        "email",
        "enrollment_date",
    ]
    cur.execute(
        "SELECT student_id, first_name, last_name, email, enrollment_date FROM students ORDER BY student_id ASC"
    )
    table.add_rows(cur.fetchall())
    print(table)
    return


def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)",
        (first_name, last_name, email, enrollment_date),
    )
    return


def updateStudentEmail(student_id, new_email):
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id)
    )
    return


def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    return


while 1:
    userChoice = int(
        input(
            "Options:\n1: Show all student info\n2: Add a student\n3: Update a student's email\n4: Delete a student\n-------\n0: Exit\nEnter a single number corresponding to the desired option:\n"
        )
    )
    match userChoice:
        case 0:
            print("\nbye-bye\n")
            break
        case 1:
            getAllStudents()
        case 2:
            first_name, last_name, email, enrollment_date = input(
                "Enter the desired student's first_name, last_name, email, and enrollment_date on a single line, seperated by single spaces:\n"
            ).split(" ")
            addStudent(first_name, last_name, email, enrollment_date)
        case 3:
            student_id, new_email = input(
                "Enter the student id followed by a single space, and then the updated email:\n"
            ).split(" ")
            updateStudentEmail(student_id, new_email)
        case 4:
            student_id = input("Enter the student id of the student to delete:\n")[0]
            deleteStudent(student_id)
        case _:
            continue
