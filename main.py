# Student Management System
# Mini Project using OOP and Decorator


# Decorator
def log_activity(func):
    def wrapper(*args, **kwargs):
        print("\n--- Activity Started ---")
        result = func(*args, **kwargs)
        print("--- Activity Completed ---")
        return result

    return wrapper


# Student Class
class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name    :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks   :", self.marks)

    def result(self):
        if self.marks >= 40:
            return "PASS"
        else:
            return "FAIL"


# Student Management Class
class StudentManagement:

    def __init__(self):
        self.students = []

    @log_activity
    def add_student(self):
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        marks = float(input("Enter marks: "))

        student = Student(name, roll_no, marks)
        self.students.append(student)

        print("Student added successfully!")

    @log_activity
    def display_students(self):

        if len(self.students) == 0:
            print("No students available.")
            return

        for student in self.students:
            print("\n-------------------")
            student.display()
            print("Result  :", student.result())


# Main Program
management = StudentManagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        management.add_student()

    elif choice == "2":
        management.display_students()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
