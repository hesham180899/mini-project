def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of n-1
        return n * factorial(n - 1)

# Example usage
def main():
    number = 5  # You can change this number to test other inputs
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")

main()
