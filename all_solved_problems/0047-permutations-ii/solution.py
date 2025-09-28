class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        counter = Counter(nums)
        def backtrack(curr):
            if len(curr) == n:
                res.append(curr[:])
                return

            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    curr.append(key)
                    backtrack(curr)
                    curr.pop()
                    counter[key] += 1
            
        backtrack([])
        return res
