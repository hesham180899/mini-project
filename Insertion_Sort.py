import random

# Function to perform Insertion Sort
def insertion_sort(arr):
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted into the sorted portion
        j = i - 1  # Index to compare the key with
        
        # Shift elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the larger element to the right
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key

# Main function
def main():
    # Generate a random list of 10 integers between 1 and 100
    arr = [random.randint(1, 100) for _ in range(10)]
    
    print("Original array:", arr)
    
    # Apply Insertion Sort
    insertion_sort(arr)
    
    print("Sorted array:", arr)

# Call the main function to execute the program
main()
