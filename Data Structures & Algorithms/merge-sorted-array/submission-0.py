class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #                    w
        #            i
        # [10,20,20,40,0,0,0,0]

        #            j
        # [12,15,22,45]

        i = m - 1
        j = n - 1
        for w in range(m + n - 1, -1, -1):
            if i < 0:
                nums1[w] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[w] = nums1[i]
                i -= 1
            else:
                if nums1[i] >= nums2[j]:
                    nums1[w] = nums1[i]
                    i -= 1
                else:
                    nums1[w] = nums2[j]
                    j -= 1