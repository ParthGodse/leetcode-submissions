class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # low, high = 0, len(nums) - 1
        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[mid] == target:
        #         return mid

        #     if nums[low] <= nums[mid]:
        #         if nums[low] <= target < nums[mid]:
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        #     else:
        #         if nums[mid] < target <= nums[high]:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        # return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
