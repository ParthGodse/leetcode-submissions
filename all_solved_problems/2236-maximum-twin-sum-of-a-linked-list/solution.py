# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        l = head
        r = head
        res = 0

        for _ in range(length//2):
            r = r.next

        prev = None
        while r:
            next_node = r.next
            r.next = prev
            prev = r
            r = next_node

        while prev:
            res = max(res, l.val + prev.val)
            l = l.next
            prev = prev.next

        return res
