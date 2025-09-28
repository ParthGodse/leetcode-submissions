from bisect import bisect_right
import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # potions.sort()
        # res = []

        # for spell in spells:
        #     # min_ = (success + spell - 1) // spell
        #     min_ = math.ceil(success / spell)
        #     idx = bisect_right(potions, min_ - 1)
        #     count = len(potions) - idx    
        #     res.append(count)

        # return res

        potions.sort()
        res = []

        def binary(potions, target):
            l, r = 0, len(potions)

            while l < r:
                mid = (l + r) // 2
                if potions[mid] * target >= success:
                    r = mid
                else:
                    l = mid + 1
            return l

        for spell in spells:
            idx = binary(potions, spell)

            res.append(len(potions) - idx)

        return res
