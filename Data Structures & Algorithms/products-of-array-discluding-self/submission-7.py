class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [0] * len(nums)
        root = nums[0]

        containsZero = False
        for i in range(1, len(nums)):
            if nums[i] == 0:
                if containsZero == True:
                    return solution

                containsZero = True
                continue
            root *= nums[i]

        for i in range(0, len(nums)):
            if nums[i] == 0:
                solution[i] = root
            elif containsZero:
                solution[i] = 0
            else:
                solution[i] = int(root / nums[i])

        return solution