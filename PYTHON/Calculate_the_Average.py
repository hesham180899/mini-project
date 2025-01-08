def calculate_average(numbers):
    # Get the sum of the list
    total_sum = sum(numbers)
    
    # Get the length of the list
    list_length = len(numbers)
    
    # Avoid division by zero in case the list is empty
    if list_length == 0:
        return 0  # Or handle it in another way if you prefer
    
    # Calculate and return the average
    return total_sum / list_length

# Example usage
def main():
    # Example list of numbers
    numbers = [10, 20, 30, 40, 50]
    
    # Call the function to calculate the average
    result = calculate_average(numbers)
    
    # Print the result
    print(f"The average of the numbers in the list is: {result}")

# Run the main function
main()
