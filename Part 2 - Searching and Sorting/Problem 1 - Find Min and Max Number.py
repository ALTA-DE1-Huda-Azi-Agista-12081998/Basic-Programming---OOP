def find_min_and_max(arr):
    if not arr:
        return "Oops! The array is empty."

    min_num = arr[0]
    max_num = arr[0]
    min_index = 0
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            min_index = i
        elif arr[i] > max_num:
            max_num = arr[i]
            max_index = i

    result = f"Min: {min_num} Index: {min_index}, Max: {max_num} Index: {max_index}."
    return result

# Sample Test Cases
print(find_min_and_max([5, 7, 4, -2, -1, 8]))
# Output: The minimum is -2 at index 3, and the maximum is 8 at index 5.

print(find_min_and_max([2, -5, -4, 22, 7, 7]))
# Output: The minimum is -5 at index 1, and the maximum is 22 at index 3.

print(find_min_and_max([4, 3, 9, 4, -21, 7]))
# Output: The minimum is -21 at index 4, and the maximum is 9 at index 2.
