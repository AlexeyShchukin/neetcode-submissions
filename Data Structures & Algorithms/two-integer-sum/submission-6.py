class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_dict and my_dict[diff] != i:
                return [i, my_dict[diff]]
        return []