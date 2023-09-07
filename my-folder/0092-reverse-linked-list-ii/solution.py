# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # if left == right:
        #     return head

        # curr = head
        # reverse = None
       
        # for i in range(right-left+1):
        #     t = curr.next
        #     curr.next = reverse
        #     reverse = curr
        #     curr = t
        # return reverse

        dummy = ListNode(0, head)

        lprev, curr = dummy , head
        for i in range(left-1):
            lprev, curr = curr, curr.next
        prev = None
        for i in range(right - left +1):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        lprev.next.next = curr
        lprev.next = prev
        return dummy.next
