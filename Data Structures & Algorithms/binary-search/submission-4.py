class Solution:
    def recursiveSearch(self, nums : list[int], target : int, min : int, max : int) -> int:
        if min > max:
            return -1

        p = int(min + (max - min) / 2)
        print(p)
        val = nums[p]

        if val == target:
            return p
    
        if val < target:
            return self.recursiveSearch(nums, target, p + 1, max)
        else:
            return self.recursiveSearch(nums, target, min, p - 1)

    def search(self, nums: List[int], target: int) -> int:
        return self.recursiveSearch(nums, target, 0, len(nums) - 1)
