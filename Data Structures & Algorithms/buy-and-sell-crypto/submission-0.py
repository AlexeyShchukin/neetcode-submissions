class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        res = 0

        for _ in range(len(prices) - 1):
            if prices[right] <= prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                res = max(profit, res)
            right += 1
        
        return res