class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod = [0]*value
        for num in nums:
            num%=value
            if num < 0:
                num += value
            mod[num] += 1
        for i in range(len(nums)):
            j = i % value
            mod[j] -= 1
            if mod[j] < 0:
                return i
        return len(nums)