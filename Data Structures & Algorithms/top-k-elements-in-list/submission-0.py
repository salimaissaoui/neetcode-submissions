class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        topk = c.most_common(k)

        res = []

        for val in topk:
            res.append(val[0])
        
        return res
        