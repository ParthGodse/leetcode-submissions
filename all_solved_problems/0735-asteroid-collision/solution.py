class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []       
        
        for num in asteroids:
            while stack and (stack[-1] > 0 and num < 0):
                top = stack[-1]
                if abs(top) > abs(num):
                    num = None
                    break
                elif abs(top) < abs(num):
                    stack.pop()
                else:
                    stack.pop()
                    num = None
                    break
            if num is not None:
                stack.append(num)

        return stack
        # res = []

        # for a in asteroids:
        #     while res and a < 0 < res[-1]:
        #         if -a > res[-1]:  # Current asteroid wins
        #             res.pop()
        #             continue
        #         elif -a == res[-1]:  # Both explode
        #             res.pop()
        #         break
        #     else:  # No collision
        #         res.append(a)

        # return res
