# Leetcode215_KthLargestElementInAnArray 数组中第K个最大元素

## 题目内容：

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

## 解题思路：

解法一：Python自带库heapq

heapq.heappush(heap, item)  把item添加到heap中（heap是一个列表）
heapq.heappop(heap)  把堆顶元素弹出，返回的就是堆顶
heapq.heappushpop(heap, item)  先把item加入到堆中，然后再pop，比 heappush() 再 heappop() 要快得多
heapq.heapreplace(heap, item)  先pop，然后再把item加入到堆中，比 heappop() 再 heappush() 要快得多
heapq.heapify(x)  将列表x进行堆调整，默认的是小顶堆
heapq.merge(*iterables)  将多个列表合并，并进行堆调整，返回的是合并后的列表的迭代器
heapq.nlargest(n, iterable, key=None)  返回最大的n个元素，是个列表 list（Top-K问题）heapq.nsmallest(n, iterable, key=None)  返回最小的n个元素，是个列表 list（Top-K问题）

### 代码：

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
		

if __name__ == '__main__':
	nums, k = [3,2,3,1,2,4,5,5,6], 4
	solu = Solution()
	print(solu.findKthLargest(nums,k))
```

