class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # l, r = 1, max(piles)
        # result = r
        # while l <= r:
        #     mid = (l + r) // 2
        #     total = 0
        #     for pile in piles:
        #         total += math.ceil(float(pile) / mid)

        #     if total <= h:
        #         result = min(result, mid)
        #         r = mid - 1
        #     else:
        #         l = mid + 1

        # return result
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(float(pile) / mid)

            if total <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


