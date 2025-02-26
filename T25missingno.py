def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
nums = [1, 2, 3, 5]
print(find_missing_number(nums))  # Output: 4