class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        count = 1  
        for i in range(2, len(nums)):
            if nums[i] != nums[count - 1]:
                count += 1
                nums[count] = nums[i]

        nums = nums[:count + 1]

        return count + 1
