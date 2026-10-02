def is_valid(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Test Case 1 - Typical case
s = "()[]{}"
print("Test Case 1:", is_valid(s))

# Test Case 2 - Edge case
s = "("
print("Test Case 2:", is_valid(s))