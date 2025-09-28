# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # values = []
        # while list1:
        #     values.append(list1.val)
        #     list1 = list1.next
        # while list2:
        #     values.append(list2.val)
        #     list2 = list2.next
        # values.sort()
        # dummy = ListNode()
        # curr = dummy
        # for value in values:
        #     curr.next = ListNode(value)
        #     curr = curr.next
        # return dummy.next
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
