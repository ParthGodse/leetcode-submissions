class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # def backtrack(curr):
        #     n = len(nums)
        #     if len(curr) == n:
        #         res.append("".join(curr))
        #         return

        #     for bit in["0", "1"]:
        #         curr.append(bit)
        #         backtrack(curr)
        #         curr.pop()

        # res = []
        # backtrack([])
        # for i in res:
        #     if i not in nums:
        #         return i
        # return []
        n =len(nums)
        res = []
        for i in range(n):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        return "".join(res)
