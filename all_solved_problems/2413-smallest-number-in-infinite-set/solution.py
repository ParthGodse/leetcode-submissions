class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.s = set()

    def popSmallest(self) -> int:
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        else:
            self.curr += 1
            return self.curr - 1

    def addBack(self, num: int) -> None:
        if self.curr > num:
            self.s.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
