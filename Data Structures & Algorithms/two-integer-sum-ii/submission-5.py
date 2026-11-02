class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while(i <= j):
            l = numbers[i]
            r = numbers[j]

            sum = l + r
            if sum == target:
                return [i + 1, j + 1]

            if sum > target:
                j -= 1
            else:
                i += 1

        # error state
        return [-1, -1]