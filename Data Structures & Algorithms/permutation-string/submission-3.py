class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        targetStringMap = {}    # char -> [found, needed]
        for c in s1:
            if c not in targetStringMap:
                targetStringMap[c] = [0, 1]
            else:
                targetStringMap[c][1] += 1
        
        valuesFound = 0
        for i in range(len(s1)):
            c = s2[i]
            if c in targetStringMap:
                targetStringMap[c][0] += 1
                if targetStringMap[c][0] <= targetStringMap[c][1]:
                    valuesFound += 1

        if valuesFound == len(s1):
            return True

        for i in range(len(s1), len(s2)):
            oldC = s2[i - len(s1)]
            print(oldC)
            if oldC in targetStringMap:
                targetStringMap[oldC][0] -= 1
                if targetStringMap[oldC][0] < targetStringMap[oldC][1]:
                    valuesFound -= 1

            newC = s2[i]
            print(newC)
            if newC in targetStringMap:
                targetStringMap[newC][0] += 1
                if targetStringMap[newC][0] <= targetStringMap[newC][1]:
                    valuesFound += 1

                if valuesFound == len(s1):
                    return True

        return False
            