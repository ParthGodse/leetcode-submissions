class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Standard Kadane to get max subarray (non-empty)  
        # Kadane for maximum subarray
        def kadane_max(arr):
            largest = arr[0]
            curr = 0

            for num in arr:
                curr += num
                largest = max(largest, curr)
                if curr < 0:
                    curr = 0

            return largest

        # Kadane for minimum subarray (reverse logic)
        def kadane_min(arr):
            smallest = arr[0]
            curr = 0

            for num in arr:
                curr += num
                smallest = min(smallest, curr)
                if curr > 0:
                    curr = 0

            return smallest

        total = sum(nums)

        max_k = kadane_max(nums)
        min_k = kadane_min(nums)

        # If all numbers are negative, the wrap-around case is invalid
        if max_k < 0:
            return max_k

        # max of: normal max subarray, or total - min subarray (wrap-around)
        return max(max_k, total - min_k)
