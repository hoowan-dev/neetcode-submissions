class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valToIndicies = dict() # val : [i, j, ...]

        for i, num in enumerate(nums):
            if num not in valToIndicies:
                valToIndicies[num] = [i]
            else:
                valToIndicies[num].append(i)

        for indicies in valToIndicies.values():
            if len(indicies) >= 2:
                for i in range(len(indicies) - 1):
                    if indicies[i + 1] - indicies[i] <= k:
                        return True

        return False
