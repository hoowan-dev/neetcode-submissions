class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestTotalArea = 0

        for i in range(len(heights)):
            if heights[i] == 0:
                continue

            largestLocalArea = heights[i]
            minHeight = heights[i]
            for j in range(i + 1, len(heights)):
                if heights[j] == 0:
                    break

                minHeight = min(minHeight, heights[j])
                localArea = (j - i + 1) * minHeight
                if localArea > largestLocalArea:
                    largestLocalArea = localArea
            
            if largestLocalArea > largestTotalArea:
                largestTotalArea = largestLocalArea
        
        return largestTotalArea