# Write an algorithm that finds the contiguous subarray within a list of numbers which has the largest sum, and returns that sum.

def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum

nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
# The contiguous subarray with the largest sum is [3, 4, -1, 2, 1], which has a sum of 9.
result = max_subarray_sum(nums) 
print(result)  
