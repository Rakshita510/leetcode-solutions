# Binary Search

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/binary-search/

## Problem

Given a sorted array of integers and a target value, return the index of the target if it exists. Otherwise, return -1.

## Approach

I use the binary search technique.

- Set the left and right boundaries of the array.
- Find the middle element.
- If the middle element is the target, return its index.
- If the middle element is smaller than the target, search the right half.
- If the middle element is greater than the target, search the left half.
- Continue until the target is found or the search range becomes empty.

## Time Complexity

O(log n)

## Space Complexity

O(1)

## Test Cases

### Test Case 1 - Typical Case

Input:
```text
nums = [-1, 0, 3, 5, 9, 12]
target = 9
```

Output:
```text
4
```

### Test Case 2 - Edge Case

Input:
```text
nums = [5]
target = 2
```

Output:
```text
-1
```

## Notes / Edge Cases

- The array must be sorted for binary search to work correctly.
- If the target is not present, the function returns -1.
- A single-element array is also handled.

## Learning Notes

I learned how binary search reduces the search area by half at each step and provides an efficient way to search a sorted array.