def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            # If we find an element that is greater than its adjacent element, then swap them
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    
    return nums

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)
print("Sorted list:", bubble_sort(numbers))