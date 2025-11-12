class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        # --- prefix products ---
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        
        # --- suffix products ---
        suffix = [1] * n
        suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        # --- diagonal combine ---
        arr1 = prefix[:-1]     # remove last from prefix
        arr2 = suffix[1:]      # remove first from suffix
        
        res = [arr2[0]]        # start with first of modified arr2
        for i in range(1, n - 1):
            res.append(arr2[i] * arr1[i - 1])
        res.append(arr1[-1])   # append second last of arr1
        
        return res
