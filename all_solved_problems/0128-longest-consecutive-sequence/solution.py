class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # nums = sorted(set(nums))
        # count = 1
        # longest = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1] + 1:
        #         count += 1
        #     else:
        #         longest = max(longest, count)
        #         count = 1

        # return max(longest, count)
        if not nums:
            return 0
        nums = sorted(set(nums))
        count = 1
        longg = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                longg = max(longg, count)
                count = 1
        return max(longg, count)
