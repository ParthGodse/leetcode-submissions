class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = count = 0

        for num in nums:
            if num == 1:
                count += 1
                maxx = max(count, maxx)
            else:
                count = 0
        return maxx
