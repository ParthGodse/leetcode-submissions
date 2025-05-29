class Solution:
    def findMin(self, nums: List[int]) -> int:
        # low, high = 0, len(nums) - 1
        # while low < high:
        #     mid = (low + high) // 2
        #     if nums[mid] < nums[high]:
        #         high = mid 
        #     else:
        #         low = mid + 1
        # return nums[low] 
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) //2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[r]
