class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        ans = 0

        while l <= r:
            mid = (l + r) //2
            total = 0
            for num in nums:
                total += math.ceil(float(num)/mid)
                if total > threshold:
                    break

            if total <= threshold:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
