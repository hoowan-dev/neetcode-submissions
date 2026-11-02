class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        digitStack = []
        for t in tokens:
            if t.lstrip("-").isdigit():
                digitStack.append(int(t))
            else:
                r = 0 if len(digitStack) == 0 else digitStack.pop()
                l = 0 if len(digitStack) == 0 else digitStack.pop()

                if t == "+":
                    l = l + r
                elif t == "-":
                    l = l - r
                elif t == "*":
                    l = l * r
                elif t == "/":
                    l = l if r == 0 else int(l / r)

                digitStack.append(l)

        return digitStack.pop()