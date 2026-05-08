class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        sequences = {}
        starts = {}

        for n in nums:
            before = sequences.pop(n-1, None)
            after = starts.pop(n+1, None)

            if before is not None and after is not None:
                merged = before + [n] + after
                starts[merged[0]] = merged
                sequences[merged[-1]] = merged
            
            elif before is not None:
                before.append(n)
                sequences[n] = before
                starts[before[0]] = before
            
            elif after is not None:
                after.insert(0, n)
                starts[n] = after
                sequences[after[-1] ] = after
            
            else:
                seq = [n]
                sequences[n] = seq
                starts[n] = seq

        seen = set()
        result = []
        for seq in sequences.values():
            key = id(seq)
            if key not in seen:
                seen.add(key)
                result.append(seq)
            
        return len(max(result, key=len))