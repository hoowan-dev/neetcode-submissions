class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappearedNumbers = set()

        for num in range(1, len(nums) + 1):
            disappearedNumbers.add(num)

        for num in nums:
            disappearedNumbers.discard(num)

        return list(disappearedNumbers)