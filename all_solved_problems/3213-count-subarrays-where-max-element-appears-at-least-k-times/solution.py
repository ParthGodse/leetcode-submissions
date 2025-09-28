class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        count = 0
        x = max(nums)

        for right in range(len(nums)):
            if nums[right] == x:
                freq[x] += 1
            # num = nums[right]
            # freq[num] += 1

            while freq[x] >= k:
                count += len(nums) - right
                if nums[left] == x:
                    freq[x] -= 1
                left += 1

        return count
