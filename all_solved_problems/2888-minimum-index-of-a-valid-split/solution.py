class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq, key=freq.get)
        total_freq = max(freq.values())
        n = len(nums)

        left = 0

        for i in range(n):
            if nums[i] == max_freq:
                left += 1

            left_len = i + 1
            right_len = n - left_len

            right = total_freq - left

            if left > left_len // 2 and right > right_len // 2:
                return i

        return -1
