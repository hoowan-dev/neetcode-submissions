class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valStack = []

        for token in tokens:
            match token:
                case "+":
                    val1 = valStack.pop()
                    val2 = valStack.pop()
                    result = val2 + val1
                case "-":
                    val1 = valStack.pop()
                    val2 = valStack.pop()
                    result = val2 - val1
                case "*":
                    val1 = valStack.pop()
                    val2 = valStack.pop()
                    result = val2 * val1
                case "/":
                    val1 = valStack.pop()
                    val2 = valStack.pop()
                    result = val2 / val1
                case _:
                    result = int(token)

            valStack.append(int(result))

        return valStack.pop()
