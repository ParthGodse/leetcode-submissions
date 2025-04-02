class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # total = 0
        # max_v = 0
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             total = (nums[i] - nums[j]) * nums[k]
        #             max_v = max(total, max_v)
        # if max_v < 0:
        #     return 0
        # else:
        #     return max_v
        max_i = nums[0]
        max_diff = float('-inf')
        max_triplet = 0
        
        for j in range(1, len(nums) - 1):
            max_diff = max(max_diff, max_i - nums[j])
            max_triplet = max(max_triplet, max_diff * nums[j + 1])
            max_i = max(max_i, nums[j])

        return max_triplet
