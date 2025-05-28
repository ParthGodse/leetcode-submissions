class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def low():    
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def high():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        left = low()
        right = high()

        if left <= right and 0 <= left < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]

        return [-1, -1]
