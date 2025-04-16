class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = 0
        window_sum = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen or right - left >= k:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            window_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

        return max_sum

