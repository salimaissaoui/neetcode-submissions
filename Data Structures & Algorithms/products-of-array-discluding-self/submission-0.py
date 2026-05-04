class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            l = nums[:i]
            if not l:
                l = [1]
            
            r = nums[i+1:]
            if not r:
                r = [1]
            
            res.append(math.prod(l) * math.prod(r))
        return res