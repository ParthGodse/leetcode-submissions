class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums)/k

        # window = sum(nums[:k])
        # max_res = window / k
        # for i in range(k, len(nums)):
        #     window += nums[i] - nums[i - k]
        #     res = window/k
        #     max_res = max(res, max_res)
        
        # return max_res
        window = sum(nums[:k])
        maxx = window

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            maxx = max(maxx, window)

        return maxx / k
