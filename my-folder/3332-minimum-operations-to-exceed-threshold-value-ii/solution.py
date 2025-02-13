class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        opr = 0

        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            new = 2 * x + y
            heapq.heappush(nums, new)
            opr += 1

        return opr 
