class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for s in strs:

            sorts = ''.join(sorted(s))

            hmap[sorts].append(s)

        return list(hmap.values())
