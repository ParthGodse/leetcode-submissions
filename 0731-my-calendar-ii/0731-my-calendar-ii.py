class MyCalendarTwo:

    def __init__(self):
        self.calendar = SortedDict()
        self.maxx_book = 2

    def book(self, startTime: int, endTime: int) -> bool:
        self.calendar[startTime] = self.calendar.get(startTime, 0) + 1
        self.calendar[endTime] = self.calendar.get(endTime, 0) - 1

        overlap = 0

        for count in self.calendar.values():
            overlap += count
            if overlap > self.maxx_book:
                self.calendar[startTime] -= 1
                self.calendar[endTime] += 1

                if self.calendar[startTime] == 0:
                    del self.calendar[startTime]

                return False
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)