class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = minSum = 0
        currentMax = currentMin = 0

        for num in nums:
            currentMax = max(num, currentMax + num)
            maxSum = max(maxSum, currentMax)

            currentMin = min(num, currentMin + num)
            minSum = min(minSum, currentMin)

        return max(abs(maxSum), abs(minSum))  # One-liner for max absolute sum
