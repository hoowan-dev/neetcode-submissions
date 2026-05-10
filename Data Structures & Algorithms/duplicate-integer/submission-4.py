class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        visited = { nums[0] }

        for i in range (1, len(nums)):
            value = nums[i]
            if value in visited:
                return True
            visited.add(value)

        return False