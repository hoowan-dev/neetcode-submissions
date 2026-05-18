class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        distinctSteps = [-1] * n

        distinctSteps[0] = 1
        distinctSteps[1] = 2

        for i in range(2, n):
            distinctSteps[i] = distinctSteps[i - 1] + distinctSteps[i - 2]

        return distinctSteps[n - 1]