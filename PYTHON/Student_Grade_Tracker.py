import os

# Function to input and store grades in a file
def input_grades():
    grades = []
    while True:
        try:
            # Input subject name and grade
            subject = input("Enter the subject name (or type 'exit' to finish): ").strip()
            if subject.lower() == 'exit':
                break

            grade = input(f"Enter the grade for {subject}: ").strip()
            # Ensure the grade is a valid number
            grade = float(grade)

            # Store the subject and grade in a tuple and add it to the grades list
            grades.append((subject, grade))

            # Save the grade to the file
            with open("grades.txt", "a") as file:
                file.write(f"{subject},{grade}\n")

        except ValueError:
            print("Invalid input! Please enter a valid numeric grade.")
        except Exception as e:
            print(f"An error occurred: {e}")
    return grades

# Function to read grades from the file and calculate the average
def calculate_average():
    try:
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as file:
                lines = file.readlines()

            grades = []
            for line in lines:
                try:
                    subject, grade = line.strip().split(',')
                    grades.append(float(grade))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

            if grades:
                average = sum(grades) / len(grades)
                print(f"Your average grade is: {average:.2f}")
            else:
                print("No valid grades available to calculate an average.")
        else:
            print("No grade records found. Please input some grades first.")
    except Exception as e:
        print(f"An error occurred while calculating the average: {e}")

# Main function to run the grade tracker program
def main():
    while True:
        print("\nGrade Tracker")
        print("1. Input new grades")
        print("2. Calculate and display average grade")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            input_grades()
        elif choice == '2':
            calculate_average()
        elif choice == '3':
            print("Exiting the Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main()
