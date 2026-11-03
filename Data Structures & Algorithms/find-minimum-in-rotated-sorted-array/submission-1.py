class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        if nums[start] <= nums[end]:
            return nums[0]
            
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1

        return nums[start]