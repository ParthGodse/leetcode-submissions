# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count=0
        temp=head
        while temp:
            temp=temp.next
            count+=1
        n=count//k #No. of groups to be reversed
        prev=dummy=ListNode()
        dummy.next=head
        while n:
            curr=prev.next
            nex=curr.next
            for i in range(1,k): #If we have to reverse k nodes then k-1 links will be reversed
                curr.next=nex.next
                nex.next=prev.next
                prev.next=nex
                nex=curr.next
            prev=curr
            n-=1
        return dummy.next
