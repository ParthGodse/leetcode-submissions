class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxx = minn = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if n < 0:
                maxx, minn = minn, maxx

            maxx = max(n, n*maxx)
            minn = min(n, n*minn)

            res = max(res, maxx)

        return res