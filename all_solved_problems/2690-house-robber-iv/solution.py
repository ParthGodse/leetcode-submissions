class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # max_values = []

        # def backtrack(start, group):
        #     if len(group) == k:
        #         max_values.append(max(group))  
        #         return
        #     for i in range(start + 2, n):  
        #         group.append(nums[i])
        #         backtrack(i, group)
        #         group.pop()  

        # for i in range(n - k + 1):  
        #     backtrack(i, [nums[i]])

        # return min(max_values)
        left, right = min(nums), max(nums)

        while left < right:
            mid = (left + right) // 2
            if self.canRob(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        
        return left

    def canRob(self, nums: List[int], k: int, capability: int) -> bool:
        count, i = 0, 0
        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 2
            else:
                i += 1
            if count >= k:
                return True
        return count >= k
