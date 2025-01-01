import random

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, no need to check them
        swapped = False
        
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped by the inner loop, the list is already sorted
        if not swapped:
            break
    
    return arr

def main():
    # Generate a random list of 10 numbers between 1 and 100
    arr = [random.randint(1, 100) for _ in range(10)]
    
    print("Original list:", arr)
    
    # Call the bubble_sort function to sort the list
    sorted_arr = bubble_sort(arr)
    
    print("Sorted list:", sorted_arr)

# Call the main function
main()
7