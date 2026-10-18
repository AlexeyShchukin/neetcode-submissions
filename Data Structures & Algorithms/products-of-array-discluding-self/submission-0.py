class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = []
        res = []
        for i in range(len(nums)):
            num = nums.pop(i)
            res.append(math.prod(nums) * math.prod(temp))
            temp.append(num)
            nums.insert(i, 1)
        return res