def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Test Case 1 - Typical case
nums = [2, 7, 11, 15]
target = 9
print("Test Case 1:", two_sum(nums, target))

# Test Case 2 - Edge case
nums = [3, 3]
target = 6
print("Test Case 2:", two_sum(nums, target))