class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        uniqueFolders = [folder[0]]
        
        for i in range(1, len(folder)):
            subfolderPrefix = uniqueFolders[-1] + '/'
            if not folder[i].startswith(subfolderPrefix):
                uniqueFolders.append(folder[i])

        return uniqueFolders
            