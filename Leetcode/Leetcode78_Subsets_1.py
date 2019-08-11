class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def temp(start, num):
            res.append(num)
            for i in range(start, len(nums)):
                temp(i+1, num+[nums[i]])
        temp(0, [])
        return res
