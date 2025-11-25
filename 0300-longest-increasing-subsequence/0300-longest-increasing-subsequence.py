class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary(res, n):
            l, r = 0, len(res) - 1

            while l <= r:
                mid = (l + r) // 2

                if res[mid] == n:
                    return mid
                elif res[mid] < n:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                ind = binary(res, n)
                res[ind] = n

        return len(res)