def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test Case 1 - Typical case
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print("Test Case 1:", binary_search(nums, target))

# Test Case 2 - Edge case
nums = [5]
target = 2
print("Test Case 2:", binary_search(nums, target))