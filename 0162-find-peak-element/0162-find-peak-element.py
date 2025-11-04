class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l, r = 0, 1

        while l <= len(nums) - 2 and r <= len(nums) - 1:
            if nums[l] < nums[r]:
                if r == len(nums) - 1:
                    return r
                r+= 1
                l+= 1
                if nums[r] < nums[l]:
                    return l
                elif nums [r] > nums[l] and r == len(nums) - 1:
                    return r
                else:
                    l += 1
                    r += 1
            elif nums[r] < nums[l]:
                return l