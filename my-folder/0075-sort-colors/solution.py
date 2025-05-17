class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        l, r = 0, n - 1
        while l <= r:
            if nums[l] == 0:
                l += 1
            elif nums[r] != 0:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        r = n - 1
        while l <= r:
            if nums[r] == 2:
                r -= 1
            elif nums[l] != 2:
                l += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums
