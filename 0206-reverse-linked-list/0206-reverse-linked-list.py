# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev: Optional[ListNode] = None) -> Optional[ListNode]:
        if not head:
            return prev
       
       
        curr = head
        next_node = curr.next
        head.next = prev

        return self.reverseList(next_node, curr)


    