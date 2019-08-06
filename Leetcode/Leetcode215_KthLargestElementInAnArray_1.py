import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
		

if __name__ == '__main__':
	nums, k = [3,2,3,1,2,4,5,5,6], 4
	solu = Solution()
	print(solu.findKthLargest(nums,k))