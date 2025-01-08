import random

# Function to merge two halves in sorted order
def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Compare elements from both halves and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Add any remaining elements from left or right
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Merge Sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Recursively sort the left half
    right = merge_sort(arr[mid:])  # Recursively sort the right half
    
    # Merge the two sorted halves
    return merge(left, right)

# Main function to generate a random array and sort it
def main():
    # Generate a random list of 10 numbers between 1 and 100
    arr = [random.randint(1, 100) for _ in range(10)]
    
    print("Original array:", arr)
    
    # Sort the array using merge sort
    sorted_arr = merge_sort(arr)
    
    print("Sorted array:", sorted_arr)

# Call the main function
main()
