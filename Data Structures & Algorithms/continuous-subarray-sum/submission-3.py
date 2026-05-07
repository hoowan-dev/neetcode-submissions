def isMultiple(sum, k):
    if sum == 0:
        return True
    return sum % k == 0

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        
        for windowSize in range(2, len(nums) + 1):
            sum = 0
            for i in range(0, windowSize):
                sum += nums[i]

            if isMultiple(sum, k):
                return True
            
            for i in range(1, len(nums) - windowSize + 1):
                sum -= nums[i - 1]
                sum += nums[i + windowSize - 1]

                if isMultiple(sum, k):
                    return True

        return False
            
        