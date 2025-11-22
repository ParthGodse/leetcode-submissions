class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visit = [False] * n

        def backtrack(curr):
            if len(curr) == n:
                res.append(curr[:])
                return

            for i in range(n):
                if not visit[i]:
                    visit[i] = True
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    visit[i] = False
        
        backtrack([])
        return res