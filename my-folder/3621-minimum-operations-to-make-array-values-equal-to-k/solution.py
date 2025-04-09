class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1

        distinct = set(nums)

        greater = sum(1 for num in distinct if num > k)

        return greater
