class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        return -1
        '''

        nums.sort()

        prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if prev == curr:
                return prev
            prev = curr

        return -1