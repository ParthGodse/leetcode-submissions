class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # result = [0] * len(temperatures)

        # for i, temp in enumerate(temperatures):
        #     while stack and temperatures[stack[-1]] < temp:
        #         pre = stack.pop()
        #         result[pre] = i - pre

        #     stack.append(i)

        # return result

        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                pre = stack.pop()
                res[pre] = i - pre
            stack.append(i)

        return res
