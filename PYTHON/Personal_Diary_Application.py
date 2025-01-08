import os
from datetime import datetime

# Function to add a new diary entry
def add_entry(diary_file):
    try:
        # Optionally add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Enter your diary entry (type 'exit' to finish):")
        
        # Get the diary entry from the user
        entry = []
        while True:
            line = input()
            if line.lower() == 'exit':
                break
            entry.append(line)
        
        # Join the entry and add the timestamp (if applicable)
        full_entry = "\n".join(entry)
        if input("Do you want to add a timestamp to this entry? (y/n): ").lower() == 'y':
            full_entry = f"{timestamp} - {full_entry}"
        
        # Save the entry to the file
        with open(diary_file, 'a') as file:
            file.write(full_entry + "\n\n")
        
        print("Your entry has been saved successfully!")

    except PermissionError:
        print("Error: You do not have permission to write to the diary file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to view previous diary entries
def view_entries(diary_file):
    try:
        if os.path.exists(diary_file):
            with open(diary_file, 'r') as file:
                content = file.read()
                if content:
                    print("\nPrevious Diary Entries:\n")
                    print(content)
                else:
                    print("No entries found in your diary.")
        else:
            print("No diary file found. Start by adding an entry.")
    except PermissionError:
        print("Error: You do not have permission to read from the diary file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the diary application
def main():
    diary_file = "diary.txt"
    
    while True:
        print("\nPersonal Diary Application")
        print("1. Add a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_entry(diary_file)
        elif choice == '2':
            view_entries(diary_file)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the application
if __name__ == "__main__":
    main()
