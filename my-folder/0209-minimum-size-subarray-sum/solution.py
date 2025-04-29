class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window, length = 0, 0
        min_len = float('inf')
        for right in range(len(nums)):
            window += nums[right]
            
            while window >= target:
                length = right - left + 1
                min_len = min(min_len, length)
                window -= nums[left]
                left += 1
                
        return 0 if min_len == float('inf') else min_len
