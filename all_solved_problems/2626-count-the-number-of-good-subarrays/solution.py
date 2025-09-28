class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        pairs = 0
        res = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            num = nums[right]
            pairs += freq[num]
            freq[num] += 1

            while pairs >= k:
                res += len(nums) - right

                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return res

