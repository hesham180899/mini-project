# Function to generate Fibonacci sequence
def fibonacci_sequence(count):
    # First two Fibonacci numbers are always 0 and 1
    a, b = 0, 1
    for i in range(count):
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update a and b to the next two Fibonacci numbers

# Main program
if __name__ == "__main__":
    try:
        count = int(input("Enter the number of Fibonacci numbers you want: "))
        if count <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence(count)  # Call the function to print the sequence
    except ValueError:
        print("Invalid input. Please enter an integer value.")
