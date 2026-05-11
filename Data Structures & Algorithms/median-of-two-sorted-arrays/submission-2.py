class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        p = int((len(nums1) + len(nums2)) / 2)
        l, r = 0, 0
        i, j = 0, 0

        if len(nums1) > 0:
            if len(nums2) > 0:
                if nums1[0] <= nums2[0]:
                    r = nums1[0]
                    i += 1
                else:
                    r = nums2[0]
                    j += 1
            else:
                r = nums1[0]
                i += 1
        else:
            r = nums2[0]
            j += 1

        #     i
        # 1 3 4
        
        #   j
        # 2 5 6

        # l, r = 2, 3
        # p = 3
        for _ in range(0, p):
            l = r
            if i >= len(nums1):
                r = nums2[j]
                j += 1
            elif j >= len(nums2):
                r = nums1[i]
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    r = nums1[i]
                    i += 1
                else:
                    r = nums2[j]
                    j += 1

        median = 0
        if (len(nums1) + len(nums2)) % 2 == 0:
            median = ((l + r) / 2)
        else:
            median = r

        return median

        '''
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
        '''
