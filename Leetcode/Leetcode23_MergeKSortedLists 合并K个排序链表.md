# Leetcode23_MergeKSortedLists 合并K个排序链表

## 题目内容：

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

## 解题思路：

### 解法一：

将K个链表的所有节点值放入到一个数组中，然后对数组进行排序，再构建一个新的链表，将其返回。

### 代码：

```python
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
```

