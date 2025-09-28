# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return

        # length = 0
        # temp = head
        # while temp:
        #     length += 1
        #     temp = temp.next
        
        # index = length // 2
        # if index == 0:
        #     head = head.next
        #     return
        
        # temp = head
        # for _ in range(index - 1):
        #     if not temp.next:
        #         return
        #     temp = temp.next

        # if not temp.next:
        #     return

        # temp.next = temp.next.next

        # return head

        if not head or not head.next:
            return None
        
        slow = head
        fast = head.next.next
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head

