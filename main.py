from database import(
    create_database,
    add_students,
    view_students,
    search_student,
    update_student,
    delete_student
)
def main():
    create_database()
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                student_id = int(input("Enter Student ID: "))
                name = input("Enter student Name: ")
                email = input("Enter Email: ")
                gpa = float(input("Enter GPA (0-10): "))
                add_students(student_id, name, email, gpa)
            elif choice == "2":
                view_students()
            elif choice == "3":
                student_id = int(input("Enter Student ID: "))
                search_student(student_id)
            elif choice == "4":
                student_id = int(input("Enter Student ID: "))
                name = input("Enter New Name: ")
                email = input("Enter New Email: ")
                gpa = float(input("Enter New GPA (0-10): "))
                update_student(student_id, name, email, gpa)
            elif choice == "5":
                student_id = int(input("Enter Student ID to delete: "))
                delete_student(student_id)
            elif choice == "6":
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice. Please select 1-6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    main()