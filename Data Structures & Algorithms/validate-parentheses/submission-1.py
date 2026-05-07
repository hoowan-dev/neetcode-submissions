class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if (len(stack) == 0):
                    return False

                opening = stack.pop()
                if (opening == '(' and c != ')') or (opening == '{' and c != '}') or (opening == '[' and c != ']'):
                    return False
        
        return len(stack) == 0