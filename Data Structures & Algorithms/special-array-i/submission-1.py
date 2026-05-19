class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        for i in range(len(nums) - 1):
            n1, n2 = nums[i], nums[i + 1]

            if n1 % 2 == n2 % 2:
                return False

        return True