class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # seen = set()
        # l, r = 0, n - 1
        # while l <= r:
        #     mid = (l + r)//2

        #     if nums[mid] > mid:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return l
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
