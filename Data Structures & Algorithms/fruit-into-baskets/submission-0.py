class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f1_first = 0
        f1_last = 0
        f2_first = 0
        f2_last = 0

        for i in range(1, len(fruits)):
            if fruits[i] == fruits[f1_first]:
                f1_last = i
            else:
                f2_first = f2_last = i
                break
                
        maxFruits = f2_last + 1

        for i in range(f2_last + 1, len(fruits)):
            if fruits[i] == fruits[f1_last]:
                f1_last = i
            elif fruits[i] == fruits[f2_last]:
                f2_last = i
            else:
                f1_first = min(f1_last, f2_last) + 1
                f1_last = max(f1_last, f2_last)
                f2_first = i
                f2_last = i

            maxFruits = max(maxFruits, max(f1_last, f2_last) - f1_first + 1)

        return maxFruits

