class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}  # {value: index}
        for i, v in enumerate(numbers):
            diff = target - v
            if diff in hashmap:
                return [hashmap[diff] + 1, i + 1]
            hashmap[v] = i
        return []
        
