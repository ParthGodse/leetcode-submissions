class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1:
            return 0
        stack = []
        res = []
        s = str(x)
        for ch in s:
            if ch.isdigit():
                stack.append(ch)
            else:
                res.append(ch)
        print(stack)
        while stack:    
            res.append(stack.pop())
        print(res)
        new =  "".join(res)
        if new == "":
            return 0
        new1= int(new) 
        return new1 if abs(new1) < 2**31 - 1 else 0