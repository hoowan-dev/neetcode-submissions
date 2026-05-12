class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = [-1, -1]

        l = 0
        r = len(numbers) - 1

        while True:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                solution[0], solution[1] = l + 1, r + 1
                break

        return solution