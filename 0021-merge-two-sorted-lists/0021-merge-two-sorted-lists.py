# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode()

        print(ans)
        print(list1)
        print(list2)

        current = ans # ans를 참조 - 같은 ListNode 객체를 가리킴

        if not list1:
            return list2
        elif not list2:
            return list1
        
        while list1 and list2:
            
            if list1.val >= list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        if list1 :
            current.next = list1
        if list2:
            current.next = list2

        print(ans)
        print(current)
        return ans.next
        # 연결 리스트 -> 첫 번째 노드 - 이후 노드 next를 통해 탐색 가능