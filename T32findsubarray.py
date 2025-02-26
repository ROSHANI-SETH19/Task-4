def find_subarray(nums, target_sum):
    window_sum = 0
    start = 0
    for end, num in enumerate(nums):
        window_sum += num
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        if window_sum == target_sum:
            return (start, end)
    return (-1, -1)

# Example usage:
nums = [1, 4, 20, 3, 10, 5]
target_sum = 33
print(find_subarray(nums, target_sum))  # Output: (2, 4)