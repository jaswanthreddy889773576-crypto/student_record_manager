import json
import os


FILE_NAME = "students.json"


# Load students from JSON file
def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data if data else []
    except json.JSONDecodeError:
        return []


# Save students to JSON file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# 1. Add Student
def add_student():
    students = load_students()

    while True:
        student_id = input("Enter student ID: ")
        duplicate = False
        for student in students:
            if student['id'] == student_id:
                duplicate = True
                break
        if duplicate:
            print('Student ID already exists. Please enter a different Id.')
        else:
            break


    name = input("Enter student name: ")

    while True:
        try:
            age = int(input("Enter student age: "))

            if age <= 0:
                print('Age must be greater than 0')
                continue

            break

        except ValueError:
            print('Please enter valid age.')

    while True:
        try:
            marks = float(input("Enter student marks: "))

            if marks < 0:
                print('Marks cannot be negative ')
                continue
            break

        except ValueError:
            print('Please enter valid marks.')


    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# 2. View Students
def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Marks: {student['marks']}"
        )


# 3. Search Student
def search_student():
    students = load_students()

    student_id = input("Enter student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found:")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


# 4. Update Student
def update_student():
    students = load_students()

    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("\n1. Update Name")
            print("2. Update Age")
            print("3. Update Marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")

            elif choice == "2":
                while True:
                    try:
                        new_age = int(input("Enter new age: "))
                        if new_age <= 0:
                            print('Age must be greater than 0')
                            continue
                        student['age'] = new_age
                        break
        
                    except ValueError:
                        print('Please enter valid age.')


            elif choice == "3":
                while True:
                    try:
                        new_marks = float(input("Enter new marks: "))
                        if new_marks < 0:
                            print('Marks cannot be negative.')
                            continue
                        student['marks'] = new_marks
                        break

                    except ValueError:
                        print('Please enter valid marks.')

            else:
                print("Invalid choice.")
                return

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found.")


# 5. Delete Student
def delete_student():
    students = load_students()

    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["id"] == student_id:

            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main menu
while True:

    print("\n==============================")
    print("     STUDENT RECORD MANAGER")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")