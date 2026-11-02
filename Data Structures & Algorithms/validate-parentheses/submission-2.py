class Solution:
    def isValid(self, s: str) -> bool:
        def isOpening(self, c) -> bool:
            return c == '(' or c == '{' or c == '['
        
        def isMatching(self, opening, closing) -> bool:
            return ((opening == '(' and closing == ')') or (opening == '{' and closing == '}')  or (opening == '[' and closing == ']') )

        stack = []

        for c in s:
            if isOpening(self, c):
                stack.append(c)
            else:
                if (len(stack) == 0) or (isMatching(self, stack.pop(), c) == False):
                    return False

        if len(stack) > 0:
            return False

        return True 

        