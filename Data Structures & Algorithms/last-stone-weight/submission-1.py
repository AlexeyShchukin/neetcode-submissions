class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone = abs(heapq.heappop_max(stones) - heapq.heappop_max(stones))
            heapq.heappush_max(stones, stone)
        
        return stones[0]