class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        foundNums = set()

        for num in nums:
            if num in foundNums:
                return True
            
            foundNums.add(num)

        return False