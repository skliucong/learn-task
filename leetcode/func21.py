# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newlist=None
        head=None
        while l1!=None or l2!=None:

            if l2==None or (l1!=None and l1.val<=l2.val):
                if newlist==None:
                    newlist=ListNode(l1.val)
                    head=newlist
                    l1=l1.next
                else:
                    newlist.next=ListNode(l1.val)
                    newlist=newlist.next
                    l1=l1.next
            else:
                if newlist == None:
                    newlist = ListNode(l2.val)
                    head = newlist
                    l2 = l2.next
                else:
                    newlist.next = ListNode(l2.val)
                    newlist = newlist.next
                    l2 = l2.next
        return head

if __name__ == '__main__':
    lis1= [1,2,4]
    lis2= [1,3,4]
    head1 = None
    head2 = None
    ln1 = None
    ln2 = None
    for item in lis1:
        if head1 == None:
            ln1 = ListNode(item)
            head1 = ln1
        else:
            lns = ListNode(item)
            ln1.next = lns
            ln1 = ln1.next
    for item in lis2:
        if head2 == None:
            ln2 = ListNode(item)
            head2 = ln2
        else:
            lns = ListNode(item)
            ln2.next = lns
            ln2 = ln2.next


    head=Solution().mergeTwoLists(head1,head2)


    while head != None:
        print(head.val)
        head = head.next
