# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levelOrderNodeValues = [[root.val]]

        currNodes = [root]
        while len(currNodes) != 0:
            nextLevelNodes = []
            nextLevelValues = []
            for node in currNodes:
                if node.left:
                    nextLevelNodes.append(node.left)
                    nextLevelValues.append(node.left.val)
                if node.right:
                    nextLevelNodes.append(node.right)
                    nextLevelValues.append(node.right.val)
            currNodes = nextLevelNodes
            if len(nextLevelValues) > 0:
                levelOrderNodeValues.append(nextLevelValues)

        return levelOrderNodeValues