# Merge Two Sorted Lists

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/

## Problem

Given the heads of two sorted linked lists, merge them into one sorted linked list and return the merged list.

## Approach

I used a dummy node and a `current` pointer.

I compare the values of both linked lists and add the smaller value to the merged list.

When one list becomes empty, I attach the remaining nodes from the other list.

## Time Complexity

O(n + m)

## Space Complexity

O(1)

## Test Cases

### Test Case 1 - Typical Case

Input:

```text
List 1: [1, 2, 4]
List 2: [1, 3, 4]

Output:
[1, 1, 2, 3, 4, 4]

Test Case 2 - Edge Case
Input:
List 1: []
List 2: [0]

Output:
[0]

Notes / Edge Cases
- One of the linked lists can be empty.
- Both linked lists contain sorted values.
- The remaining nodes are attached when one list becomes empty.
Learning Notes
I learned how to merge two sorted linked lists efficiently using pointers and a dummy node.