class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {} # sortedStr : List[str]

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in anagramGroups:
                anagramGroups[sortedStr].append(s)
            else:
                anagramGroups[sortedStr] = [s]

        sol = []
        for group in anagramGroups.values():
            sol.append(group) 

        return sol