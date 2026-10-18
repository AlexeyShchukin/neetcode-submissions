class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        heap_copy = self.nums.copy()
        for _ in range(self.k):
            max_val = -heapq.heappop(heap_copy)
        return max_val
