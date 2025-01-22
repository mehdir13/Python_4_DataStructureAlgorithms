# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Insertion Sort
def insertion_sort(arr):
    sorted_array = []  # Start with an empty array to build the sorted result

    for num in arr:
        # Find the correct position in sorted_array for the current number
        inserted = False
        for i in range(len(sorted_array)):
            if num < sorted_array[i]:
                sorted_array.insert(i, num)  # Insert num at the correct position
                inserted = True
                break
        if not inserted:
            sorted_array.append(num)  # Append at the end if num is the largest so far

    return sorted_array


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Example usage
example_array = [64, 34, 25, 12, 22, 11, 90]


print(
    "Bubble Sorted array:", bubble_sort(example_array[:])
)  # Use copy of array to avoid modifying original
print("Insertion Sorted array:", insertion_sort(example_array[:]))
print("Selection Sorted array:", selection_sort(example_array[:]))
