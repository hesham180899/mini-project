# Function to calculate the factorial of a number
def calculate_factorial(n):
    factorial = 1  # Initialize factorial as 1 (as 0! and 1! are both 1)
    for i in range(1, n + 1):  # Loop from 1 to n
        factorial *= i  # Multiply factorial by the current number i
    return factorial

# Main program
if __name__ == "__main__":
    try:
        # Take input from the user for the number
        number = int(input("Enter a number to calculate its factorial: "))
        
        # Check if the number is non-negative
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calculate the factorial using the function
            result = calculate_factorial(number)
            # Print the factorial result
            print(f"The factorial of {number} is {result}.")
    except ValueError:
        # Handle invalid input (if user enters non-integer)
        print("Invalid input. Please enter an integer value.")
