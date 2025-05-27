class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # freq = Counter(nums)
        # for i in freq:
        #     if freq[i] > (n/2):
        #         return i
        # nums.sort()
        # return nums[n//2]
        count = 0
        candy = 0

        for num in nums:
            if count == 0:
                candy = num

            if num == candy:
                count += 1
            else:
                count -= 1
        return candy
