def check_balanced_parentheses(s):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or parentheses_map[char] != stack.pop():
                return False

    return not stack

# Example usage:
s = "({[]})"
print(check_balanced_parentheses(s))  # Output: True

s = "({[})"
print(check_balanced_parentheses(s))  # Output: False