import time
import json

def linear_search(input, target):
    for index, value in enumerate(input):
        if value == target:
            return index  # Return the index of the target
    return -1  # Return -1 if the target is not found


def binary_search(input, target):
    leftBound, rightBound = 0, len(input) - 1
    
    while leftBound <= rightBound:
        guess = (leftBound + rightBound) // 2 # We guess the element that is in middle.
        
        if input[guess] == target:
            return guess  # Return the index of the target
        elif input[guess] < target:
            leftBound = guess + 1  # Search in the right half
        else:
            rightBound = guess - 1  # Search in the left half
            
    return -1  # Return -1 if the target is not found

# Load the list from the JSON file
with open('unsorted.json') as f:
    unsorted_list = json.load(f)

with open("sorted.json") as f:
    sorted_list = json.load(f)

# Target to search for
target = 5851136  # Change this value to test different targets

# Timing Linear Search
start_time = time.time()
linear_result = linear_search(unsorted_list, target)
linear_time = time.time() - start_time

# Timing Binary Search
start_time = time.time()
binary_result = binary_search(sorted_list, target)
binary_time = time.time() - start_time

# Results
print(f"Linear Search: Element {target} found at index {linear_result}. Time taken: {linear_time:.6f} seconds.")
print(f"Binary Search: Element {target} found at index {binary_result}. Time taken: {binary_time:.6f} seconds.")