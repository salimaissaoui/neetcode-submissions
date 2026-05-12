class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        maxSeen = 0
        for i in range(n):
            maxSeen = max(maxSeen, height[i])
            maxLeft[i] = maxSeen

        maxSeen = 0
        for i in range(n-1, -1, -1):
            maxSeen = max(maxSeen, height[i])
            maxRight[i] = maxSeen
        
        res = 0
        for i in range(n):
            
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                res += water


        return res
