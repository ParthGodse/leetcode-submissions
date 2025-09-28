class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        maximumfreq = 0
        currk = nums.count(k)
        for i in range(51):
            if i == k:
                continue
            currmax = 0
            curr = 0
            for num in nums:
                if i == num:
                    curr += 1
                elif num == k:
                    curr -= 1
                currmax = max(currmax, curr)
                curr = max(0, curr)
            maximumfreq = max(maximumfreq, currmax)
        return maximumfreq + currk 
