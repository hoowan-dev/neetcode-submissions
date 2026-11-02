class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqBuckets = {} # frequency : set_of_nums
        freqCounts = {} # num : frequency
        
        for num in nums:
            freq = 0
            if num not in freqCounts:
                freq = 1
            else:
                freqBuckets[freqCounts[num]].remove(num)
                freq = freqCounts[num] + 1

            freqCounts[num] = freq

            if freq not in freqBuckets:
                freqBuckets[freq] = set()

            freqBuckets[freq].add(num)

        topKMostFreq = []
        for freq, nums in reversed(freqBuckets.items()):
            for num in nums:
                topKMostFreq.append(num)
            if len(topKMostFreq) >= k:
                break

        return topKMostFreq

            

            