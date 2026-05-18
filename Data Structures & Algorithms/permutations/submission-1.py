class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def permuteRec(currPermutation: List[int], used: List[bool]):
            if len(currPermutation) == len(nums):
                permutations.append(currPermutation.copy())
                return

            for i, n in enumerate(used):
                if used[i] == False:
                    currPermutation.append(nums[i])
                    used[i] = True

                    permuteRec(currPermutation, used)

                    currPermutation.pop()
                    used[i] = False

        permuteRec([], [False] * len(nums))
        return permutations