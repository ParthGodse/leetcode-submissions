class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences) + 1
        prefix = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + differences[i - 1]
            # print(prefix)
        minp = min(prefix)
        maxp = max(prefix)
        start = lower - minp
        end = upper - maxp

        # for p in prefix:
        #     original = p + start

        # for p in prefix:
        #     ori = p + end

        return max(0, end - start + 1)
        

        
