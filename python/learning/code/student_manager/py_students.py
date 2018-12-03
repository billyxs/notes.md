STUDENT_FILE_NAME = "students.txt"
students = []

def add_student(name, id):
    if (name and id):
        student = { "name": name, "id": id }
        students.append(name)


def print_students_titlecase():
    for student in students:
        print(student.title())


def save_file(student):
    try:
        f = open(STUDENT_FILE_NAME, "a")
        f.write(student + "\n")
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open(STUDENT_FILE_NAME, "r")
        for student in f.readlines():
            add_student(student, 111)
        f.close()
    except Exception:
        print("Could not read file")


# Main
read_file()
print_students_titlecase()
confirm = input("Would you like to add a student?")
if confirm == 'Yes' or confirm == 'yes' or confirm == 'y':
    student_name = input("Student name?")
    student_id = input("Student id?")
    add_student(student_name, student_id)
    save_file(student_name)
else:
    print("maybe next time")




