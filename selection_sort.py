def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # return []

    n = len(arr)
    for i in range(n):  # loop runs from i=0 to i=n-1
        min_index = i  # assuming first element of unsorted portion (arr[i]) is minimum
        for j in range(i + 1,
                       n):  # This loop runs from j = i+1 to j = n-1. It finds the smallest element in the unsorted portion of the array.
            if arr[j] < arr[min_index]:  # Find the minimum element in the remaining unsorted array
                min_index = j  # Update the index of the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the element at i  with the element at min_index .
    return arr


arr = [5, 8, 3, 9, 4, 1, 7]
sorted_array = selection_sort(arr)
print(sorted_array)

# output
# [1, 3, 4, 5, 7, 8, 9]


# For selection sort:
#
# 	•	Best Case Time Complexity: Theta(n^2)
# 	•	Average Case Time Complexity: Theta(n^2)
# 	•	Worst Case Time Complexity: Theta(n^2)