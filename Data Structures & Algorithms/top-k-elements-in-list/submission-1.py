class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [(val, key) for key, val in collections.Counter(nums).items()]
        l.sort(reverse = True)
        res = []
        for i in range(k):
                res.append(l[i][1])
        return res
