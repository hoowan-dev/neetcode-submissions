class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreqMap = {} # num -> freq

        for i in nums:
            if i in numToFreqMap:
                numToFreqMap[i] += 1
            else:
                numToFreqMap[i] = 1

        # freq -> num
        freqToNumMap = {} # freq -> [] of nums
        for num, freq in numToFreqMap.items():
            if freq in freqToNumMap:
                freqToNumMap[freq].append(num)
            else:
                freqToNumMap[freq] = [num]

        topFreqs = sorted(freqToNumMap.keys(), reverse = True)[:k]
        result = [0] * k
        resultIndex = 0
        for i in range(len(topFreqs)):
            for j in freqToNumMap[topFreqs[i]]:
                result[resultIndex] = j
                resultIndex += 1
            if resultIndex >= k:
                break

        return result
        