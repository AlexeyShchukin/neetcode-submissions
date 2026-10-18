class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         flag = False
         flag = any(True for val in collections.Counter(nums).values() if val > 1)
         return flag