class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        i = 0 
        for right in range(len(nums)):

            # if nums[left] != 0:
            #     left = right
            # if nums[right] == 0:
            #     continue
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
