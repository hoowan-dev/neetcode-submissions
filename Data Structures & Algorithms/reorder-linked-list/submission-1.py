# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head: Optional[ListNode]) -> None:
        n = head
        while n:
            print(n.val)
            n = n.next
        print("_")

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None or head.next.next == None:
            return

        # count length
        a = head
        length = 0
        while a:
            a = a.next
            length += 1
        
        # split lists into two halves, a and b
        a = head
        b = a
        sizeA = length // 2
        if length % 2 == 0:
            sizeA -= 1
        for i in range(sizeA):
            b = b.next

        # split the connection
        bNextTmp = b.next
        b.next = None
        b = bNextTmp

        self.printList(a)
        self.printList(b)

        # reverse b
        curr = b
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        b = prev

        # merge both lists
        while a:
            nextA = a.next
            nextB = None
            if b:
                nextB = b.next

            a.next = b

            if b:
                b.next = nextA

            a = nextA
            b = nextB

        '''
        # create two disjoint linked lists that link every other element
        a = head
        b = head.next
        aTemp = a
        bTemp = b
        while a and b:
            a.next = b.next
            if a.next:
                b.next = a.next.next
            else:
                b.next = None

            a = a.next
            b = b.next
        a = aTemp
        b = bTemp

        self.printList(a)
        self.printList(b)

        # reverse list b
        curr = b
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        b = prev

        self.printList(b)

        # merge a and reversed b
        while a:
            nextA = a.next
            nextB = None
            if b:
                nextB = b.next

            a.next = b

            if b:
                b.next = nextA

            a = nextA
            b = nextB

        self.printList(head)
        '''
