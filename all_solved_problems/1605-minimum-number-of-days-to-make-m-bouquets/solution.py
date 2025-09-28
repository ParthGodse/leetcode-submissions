class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        l, r = min(bloomDay), max(bloomDay)
        n = len(bloomDay)
        ans = -1

        while l <= r:
            mid = l + (r - l)//2

            count = 0
            total = 0
            for day in bloomDay:
                if day <= mid:
                    count += 1
                    if count == k:
                        total += 1
                        count = 0
                else:
                    count = 0

            if total >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
