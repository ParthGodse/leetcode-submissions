class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # l, r = 0, n
        # while l < r:
        #     mid = (l + r) // 2
        #     if nums[mid] - nums[mid - 1] == 1:
        #         return nums[mid]
        #     elif nums[mid] - nums[mid - 1] > 0:                
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return r
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
