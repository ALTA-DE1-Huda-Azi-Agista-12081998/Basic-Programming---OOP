def max_sequence(nums):
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

print (max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6 
print (max_sequence ([-2, -5, 6, -2, -3, 1, 5, -6])) # 7 
print (max_sequence ([-2, -3, 4, -1, -2, 1, 5, -3])) # 7 
print (max_sequence ([-2, -5, 6, -2, -3, 1, 6, -6])) # 8
print (max_sequence ([-2, -5, 6, 2, -3, 1, 6, -6])) # 12