# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
        nodes = sorted(nodes)
        for x in nodes:
            point.next = ListNode(x)
            point = point.next
        return head.next