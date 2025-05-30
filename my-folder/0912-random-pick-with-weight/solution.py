class Solution:

    def __init__(self, w: List[int]):
        # self.w = w
        # denominator = sum(self.w)
        # for i in range(len(self.w)):
        #     self.w[i] = self.w[i] / denominator

        # # for i in range(1, len(self.w)):
        # #     self.w[i] += self.w[i - 1]
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # N = random.uniform(1, sum(self.w))

        # flag = 1
        # index = -1
        # while flag:
        #     index += 1

        #     if N <=self.w[index]:
        #         flag = 0
        # return index
        r = random.uniform(0, self.total)
        return bisect.bisect_left(self.prefix, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
