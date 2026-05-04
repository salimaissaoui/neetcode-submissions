class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        topk = c.most_common(k)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in c.items():
            buckets[freq].append(num)
        
        
        res = []

        for i in range(len(buckets) -1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                k -= 1
                if k == 0:
                    return res
        return res
        