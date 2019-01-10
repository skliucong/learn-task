#a little difficult😭
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next==None:
            return None


        ln = head
        index=0


        pren=None
        pre=None

        while ln!=None:

            if index>=n and ln!=None:
                if pren==None:
                    pren=head
                pre = pren
                pren=pren.next
            ln = ln.next
            index = index + 1

        if pren==None:
            head=head.next
            return head

        elif n==1:
            pre.next=None
        else:
            ch=pre.next
            pre.next=ch.next

        return head







if __name__ == '__main__':
    lis=[1,2,3]
    head=None
    ln=None
    for item in lis:
        if head==None:
            ln = ListNode(item)
            head=ln
        else:
            lns=ListNode(item)
            ln.next=lns
            ln=ln.next
    hea=Solution().removeNthFromEnd(head,2)

    while hea!=None:
        print(hea.val)
        hea=hea.next




