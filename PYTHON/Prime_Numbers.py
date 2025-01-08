import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):  # Check divisibility from 2 to sqrt(num)
        if num % i == 0:
            return False
    return True

# Main program
if __name__ == "__main__":
    try:
        # Take input from the user for the upper limit
        N = int(input("Enter the number up to which you want to find prime numbers: "))
        
        # Check if N is less than 2
        if N < 2:
            print("No prime numbers less than 2.")
        else:
            print(f"Prime numbers between 2 and {N} are:")
            for num in range(2, N + 1):  # Loop from 2 to N
                if is_prime(num):
                    print(num, end=" ")  # Print the prime number
            print()  # Print a newline at the end
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid integer.")
