class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # freq = Counter(nums)
        # count = 0

        # for r in nums:
        #     l = k - r
        #     if freq[l] > 0 and freq[r] > 0:
        #         if l == r and freq[r] < 2:
        #             continue
        #         count += 1
        #         freq[l] -= 1
        #         freq[r] -= 1
        #         # print(r, l,count, freq[r], freq[l])
        # return count
        nums.sort()  
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            total = nums[left] + nums[right]
            
            if total == k:  
                count += 1
                left += 1  
                right -= 1  
                
            elif total < k:  
                left += 1
            else:  
                right -= 1

        return count
