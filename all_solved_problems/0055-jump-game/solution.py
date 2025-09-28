class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # target = n - 1
        # for i in range(n - 2, -1, -1):
        #     if i + nums[i] >= target:
        #         target = i

        # return True if target == 0 else False

        jump = 0
        for num in nums:
            if jump < 0:
                return False
            elif jump < num:
                jump = num
            jump -= 1

        return True
