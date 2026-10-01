# Valid Palindrome

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/valid-palindrome/

## Problem

Given a string, determine whether it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

## Approach

I first remove characters that are not letters or numbers.

Then:
- Convert the remaining characters to lowercase.
- Reverse the cleaned string.
- Compare the cleaned string with its reverse.
- If both are equal, the string is a palindrome.

## Time Complexity

O(n)

## Space Complexity

O(n)

## Test Cases

### Test Case 1 - Typical Case

Input:
```text
s = "A man, a plan, a canal: Panama"
```

Output:
```text
True
```

### Test Case 2 - Edge Case

Input:
```text
s = " "
```

Output:
```text
True
```

## Notes / Edge Cases

- Uppercase and lowercase letters are treated as the same.
- Spaces and punctuation are ignored.
- A string containing only spaces is considered a palindrome.

## Learning Notes

I learned how to clean and process strings using Python and how to check whether a string reads the same forward and backward.