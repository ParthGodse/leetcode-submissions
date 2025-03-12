class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def negative(nums):
            left, right = 0, len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid
            return left

        def positive(nums):
            left , right = 0 , len(nums)

            while left < right:
                mid = left + (right -  left) // 2

                if nums[mid] <= 0:  
                    left = mid + 1
                else:
                    right = mid
            return len(nums) - left

        neg = negative(nums)
        pos = positive(nums)

        return max(pos, neg)
