# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True

        if (p == None and q != None) or (p != None and q == None):
            return False

        leftStack = [p]
        rightStack = [q]

        while len(leftStack) > 0 and len(rightStack) > 0:
            pNode = leftStack.pop()
            qNode = rightStack.pop()

            if pNode.val != qNode.val:
                return False

            if (pNode.left == None and qNode.left != None) or (pNode.left != None and qNode.left == None):
                return False

            if (pNode.right == None and qNode.right != None) or (pNode.right != None and qNode.right == None):
                return False
            
            if pNode.left:
                leftStack.append(pNode.left)

            if pNode.right:
                leftStack.append(pNode.right)

            if qNode.left:
                rightStack.append(qNode.left)

            if qNode.right:
                rightStack.append(qNode.right)

        return len(leftStack) == len(rightStack)