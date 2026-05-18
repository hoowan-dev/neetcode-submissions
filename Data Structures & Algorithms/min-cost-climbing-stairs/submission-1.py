class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCosts = cost.copy()

        for i in range(len(cost) - 3, -1, -1):
            minCosts[i] += min(minCosts[i + 1], minCosts[i + 2])

        return min(minCosts[0], minCosts[1])