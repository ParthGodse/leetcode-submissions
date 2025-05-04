class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # num = [0] * 100
        # res = 0
        # for x, y in dominoes:
        #     val = x * 10 + y if x <= y else y * 10 + x
        #     res += num[val]
        #     num[val] += 1
        # return res
        freq = defaultdict(int)
        count = 0
        for x, y in dominoes:
            key = tuple(sorted((x, y)))
            count += freq[key]
            freq[key] += 1
        return count
