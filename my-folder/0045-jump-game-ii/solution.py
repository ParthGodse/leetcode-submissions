class Solution:
    def jump(self, nums: List[int]) -> int:
        begin = end = jumps = 0

        while end < len(nums) - 1:
            farthest = 0
            for i in range(begin, end + 1):
                farthest = max(farthest, i + nums[i])

            begin = end + 1
            end = farthest
            jumps += 1

        return jumps
