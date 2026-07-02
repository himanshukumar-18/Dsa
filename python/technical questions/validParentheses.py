def validParenthesis(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif not stack or stack[-1] != pairs[ch]:
            return False
        else:
            stack.pop()

    return len(stack) == 0


print(validParenthesis("{[()]}"))