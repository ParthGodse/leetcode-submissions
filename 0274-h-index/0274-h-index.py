class Solution:
    def hIndex(self, citations: List[int]) -> int:
            
        citations.sort()
        n = len(citations)
        res = 0
        for i, cite in enumerate(citations):
            h = min(cite, n - i)
            res = max(res, h)
        return res