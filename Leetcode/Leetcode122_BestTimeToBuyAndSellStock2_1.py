class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        res = 0
        small = prices[0]
        for n in prices[1:]:
            if small < n:
                res += n-small 
                small = n
            else:
                small = n
        return res
