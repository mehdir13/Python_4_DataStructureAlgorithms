# 1. Brute Force Approach
# This approach checks each possible pair of numbers to see if they add up to the target.
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None  # Return None if no solution found


# 2. Dictionary approach
# This approach uses a dictionary to store each number and its index for faster lookups.
# We only really need to know if the complement exists.
def two_sum_dictionary(nums, target):
    seen_numbers = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen_numbers:
            return [seen_numbers[complement], i]
        seen_numbers[num] = i
    return None  # Return None if no solution found


# Example usage
nums = [2, 7, 11, 15]
target = 9

print("Brute Force Result:", two_sum_brute_force(nums, target))  # Output: [0, 1]
print("Hash Map Result:", two_sum_dictionary(nums, target))  # Output: [0, 1]
