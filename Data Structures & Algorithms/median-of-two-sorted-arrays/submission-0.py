class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combinedList = []

        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                combinedList.append(nums2[j])
                j += 1
            elif j == len(nums2):
                combinedList.append(nums1[i])
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    combinedList.append(nums1[i])
                    i += 1
                else:
                    combinedList.append(nums2[j])
                    j += 1

        median = 0
        if len(combinedList) == 0:
            median = 0
        elif len(combinedList) == 1:
            median = combinedList[0]
        else:
            p = int(len(combinedList) / 2)
            if len(combinedList) % 2 == 1:
                median = combinedList[p]
            else:
                median = (combinedList[p] + combinedList[p - 1]) / 2

        return median
