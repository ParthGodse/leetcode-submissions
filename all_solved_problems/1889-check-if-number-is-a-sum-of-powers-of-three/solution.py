class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        base = 3
        result = 0
        exp = 0

        while n > 0:
            remainder = n % base  
            if remainder > 1:  
                return False  
            if remainder == 1:
                result += base ** exp
            n //= base 
            exp += 1  

        return True 
