# Two Sum

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/two-sum/

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers whose sum is equal to the target.

## Approach

I used two nested loops.

- The first loop selects the first number.
- The second loop checks the numbers after it.
- If the sum of the two numbers equals the target, their indices are returned.
- If no pair is found, an empty list is returned.

## Time Complexity

O(n²)

## Space Complexity

O(1)

## Test Cases

### Test Case 1 - Typical Case

Input:

```text
nums = [2, 7, 11, 15]
target = 9
### Test Case 1 - Typical Case

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]