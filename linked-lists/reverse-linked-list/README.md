# Reverse Linked List

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/reverse-linked-list/

## Problem

Given the head of a singly linked list, reverse the linked list and return the reversed list.

## Approach

I used three pointers:

- `prev` stores the previous node.
- `current` stores the current node.
- `next_node` temporarily stores the next node.

For each node, I change its `next` pointer to point to the previous node. This continues until all nodes are reversed.

## Time Complexity

O(n)

## Space Complexity

O(1)

## Test Cases

### Test Case 1 - Typical Case

Input:

```text
[1, 2, 3, 4, 5]
Output:
[5, 4, 3, 2, 1]

Test Case 2 - Edge Case
Input:
[1]

Output:
[1]

Notes / Edge Cases
- An empty linked list should return None.
- A linked list with one node remains unchanged.
- The original links are reversed using constant extra space.
Learning Notes
I learned how to reverse a singly linked list using pointers and how to modify node connections efficiently.