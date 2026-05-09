class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        bestPrice = 0

        for i in range(1, len(prices)):
            salePrice = prices[i] - min

            if salePrice > bestPrice:
                bestPrice = salePrice

            if prices[i] < min:
                min = prices[i]

        return bestPrice