class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         return False

        # return True
        nums_i = nums_j = float('inf')
        for num in nums:
            if num <= nums_i:
                nums_i = num
            elif num <= nums_j:
                nums_j = num
            else:
                return True
        return False
