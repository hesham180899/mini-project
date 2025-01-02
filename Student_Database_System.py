# Class definition for Student
class Student:
    def __init__(self, name, age, grades=None):
        """Initialize the student object with name, age, and grades."""
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def display_info(self):
        """Display information about the student."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")
        
    def average_grade(self):
        """Calculate and return the average grade of the student."""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0

# Class for Student Database
class StudentDatabase:
    def __init__(self):
        """Initialize the database to store students."""
        self.students = []

    def add_student(self, student):
        """Add a new student to the database."""
        self.students.append(student)
    
    def display_all_students(self):
        """Display all students in the database."""
        if not self.students:
            print("No students in the database.")
        else:
            for student in self.students:
                student.display_info()
                print(f"Average Grade: {student.average_grade():.2f}")
                print("-" * 40)

# Main function to simulate the scenario
def main():
    # Create an instance of StudentDatabase
    student_db = StudentDatabase()

    # Add some students to the database
    student1 = Student("Alice", 20, [85, 90, 88])
    student2 = Student("Bob", 22, [78, 82, 80])
    
    student_db.add_student(student1)
    student_db.add_student(student2)

    # Display all students in the database
    print("Displaying all students in the database:")
    student_db.display_all_students()

    # Add a new student and display again
    student3 = Student("Charlie", 21, [92, 95, 96])
    student_db.add_student(student3)

    print("\nDisplaying all students after adding Charlie:")
    student_db.display_all_students()

# Run the main function
if __name__ == "__main__":
    main()
