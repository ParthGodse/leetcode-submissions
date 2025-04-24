class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))

        def sliding(target: int) -> int:
            freq = defaultdict(int)
            res, left, distinct = 0, 0, 0

            for right, x in enumerate(nums):
                if freq[x] == 0:
                    distinct += 1
                freq[x] += 1

                while distinct > target:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                res += (right - left + 1)

            return res

        return sliding(target) - sliding(target - 1)
