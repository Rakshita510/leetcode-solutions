def is_palindrome(s):
    cleaned = ""

    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


# Test Case 1 - Typical case
s = "A man, a plan, a canal: Panama"
print("Test Case 1:", is_palindrome(s))

# Test Case 2 - Edge case
s = " "
print("Test Case 2:", is_palindrome(s))