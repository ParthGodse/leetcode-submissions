class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # pos = []
        # neg = []
        # for num in nums:
        #     if num < 0:
        #         neg.append(num)
        #     elif num > 0:
        #         pos.append(num)
        # merged = []
        # for a, b in zip(pos, neg):
        #     merged.append(a)
        #     merged.append(b)
        # return merged
        res = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                res[pos] = num
                pos += 2
            else:
                res[neg] = num
                neg += 2
        return res
