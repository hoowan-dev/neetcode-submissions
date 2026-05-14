# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minVal = 1001
        minIndex = -1
        for i, node in enumerate(lists):
            if node != None and node.val < minVal:
                minVal = node.val
                minIndex = i
        
        head = None
        if minIndex != -1:
            head = lists[minIndex]
            lists[minIndex] = lists[minIndex].next

        if head == None:
            return None

        curr = head
        while True:
            minVal = 1001
            minIndex = -1
            for i, node in enumerate(lists):
                if node != None and node.val < minVal:
                    minVal = node.val
                    minIndex = i
            if minIndex != -1:
                tmp = lists[minIndex]
                lists[minIndex] = lists[minIndex].next
                curr.next = tmp
                curr = curr.next
            else:
                break

        return head