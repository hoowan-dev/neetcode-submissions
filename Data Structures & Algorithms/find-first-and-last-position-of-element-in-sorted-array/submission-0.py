class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sol = [-1, -1]

        for i, n in enumerate(nums):
            if n == target:
                if sol[0] == -1:
                    sol[0] = i
                sol[1] = i
            elif n > target:
                break

        return sol