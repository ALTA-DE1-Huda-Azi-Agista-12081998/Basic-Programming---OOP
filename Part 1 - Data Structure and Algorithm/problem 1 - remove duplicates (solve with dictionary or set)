def remove_duplicates(nums):
    # Check if the array is empty
    if not nums:
        return 0

    # Initialize pointers
    non_duplicate_index = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous one, update the array
        if nums[i] != nums[i - 1]:
            nums[non_duplicate_index] = nums[i]
            non_duplicate_index += 1

    # Return the length of the subarray with no duplicates
    return non_duplicate_index

print (remove_duplicates ([2, 3, 3, 3, 6, 9, 9])) # 4
print (remove_duplicates ([2, 3, 4, 5, 6, 9, 91])) # 6
print (remove_duplicates ([2, 2, 2, 11])) # 2
print (remove_duplicates ([2, 2, 2, 11])) # 2
print (remove_duplicates ([1, 2, 3, 11, 11])) # 4