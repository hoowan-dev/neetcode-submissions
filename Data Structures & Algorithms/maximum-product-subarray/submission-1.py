class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = [] # [[largestPos, largestNeg],...]
        if nums[0] >= 0:
            memo.append([nums[0], 0])
        else:
            memo.append([0, nums[0]])

        maxProduct = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            prevPos = memo[i - 1][0]
            prevNeg = memo[i - 1][1]

            maxPos, maxNeg = 0, 0
            if num >= 0:
                maxPos = max(num, prevPos * num)
                minNeg = min(num, prevNeg * num)
            else:
                maxPos = max(num, prevNeg * num)
                minNeg = min(num, prevPos * num)

            memo.append([maxPos, minNeg])
            if maxPos > maxProduct:
                maxProduct = maxPos

        print(memo)
        return maxProduct
