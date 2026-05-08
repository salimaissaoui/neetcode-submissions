class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for i in range(len(nums)):
            l = 0
            r = len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                    continue
                
                if r == i:
                    r -= 1
                    continue
                
                s = nums[l] + nums[i] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.add(tuple(sorted([nums[l],nums[r],nums[i]])))
                    l += 1
                    r -= 1
        
        return [list(t) for t in res]