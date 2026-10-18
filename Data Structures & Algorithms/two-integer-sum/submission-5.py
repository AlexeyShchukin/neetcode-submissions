class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = [(num, i) for i, num in enumerate(nums)]
        l.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if l[left][0] + l[right][0] == target:
                return [min(l[left][1], l[right][1]), max(l[left][1], l[right][1])]
            elif l[left][0] + l[right][0] > target:
                right -= 1
            else:
                left += 1
        return []