def fibonacci(n):
    # Base case: Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: Fibonacci of n is the sum of Fibonacci of n-1 and n-2
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
def main():
    number = 6  # Example: Find the 6th Fibonacci number
    result = fibonacci(number)
    print(f"The Fibonacci number at position {number} is: {result}")

main()
