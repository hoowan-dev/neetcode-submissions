class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            p = l + ((r - l) // 2)

            if nums[p] < target:
                l = p + 1
            elif nums[p] > target:
                r = p - 1
            else:
                return p

        return -1
