class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        prev, res = 0, 0
        count = 1

        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                count += 1
            else:
                res = max(res, count//2, min(prev, count))
                prev = count
                count = 1
        res = max(res, count//2, min(prev, count))
        return res