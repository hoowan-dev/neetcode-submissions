class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = { str(sorted(strs[0])) : [0] }

        for i in range(1, len(strs)):
            sortedString = str(sorted(strs[i]))

            if sortedString in anagramDict:
                anagramDict[sortedString].append(i)
            else:
                anagramDict[sortedString] = [i]
        
        result = []
        for sortedStr, indices in anagramDict.items():
            resultStrings = []
            for i in indices:
                resultStrings.append(strs[i])
            result.append(resultStrings)

        return result