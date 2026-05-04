
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for st in strs:
            c = Counter(st)
            anagrams[frozenset(c.items())].append(st)
        
        return list(anagrams.values())


         