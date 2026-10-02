# Min Stack

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/min-stack/

## Problem

Design a stack that supports the following operations:

- `push`
- `pop`
- `top`
- `getMin`

The `getMin` operation should return the minimum element in the stack.

## Approach

I used two stacks:

- `stack` stores all the elements.
- `min_stack` stores the minimum elements.

When a new value is pushed, it is also added to `min_stack` if it is smaller than or equal to the current minimum.

When the minimum value is removed, it is also removed from `min_stack`.

This allows the minimum element to be obtained efficiently.

## Time Complexity

- `push`: O(1)
- `pop`: O(1)
- `top`: O(1)
- `getMin`: O(1)

## Space Complexity

O(n)

## Test Cases

### Test Case 1 - Typical Case

Operations:

```text
push(-2)
push(0)
push(-3)
getMin()
pop()
top()
getMin()

## Notes / Edge Cases

- The stack can contain negative numbers.
- Duplicate minimum values are handled correctly.
- `getMin()` always returns the current minimum element.

## Learning Notes

I learned how two stacks can be used together to perform stack operations and retrieve the minimum element in constant time.