class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left > right:
            return [-1, -1]
            
        primes = []
        sieve = [True] * (right + 1) 
        sieve[0], sieve[1] = False, False
        
        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right + 1, i):
                    sieve[j] = False
        
        for num in range(left, right + 1):  
            if sieve[num]:
                primes.append(num)
    
        if len(primes) < 2:
            return [-1, -1]
        
        mini = float('inf')
        res = []
        
        for i in range(len(primes) - 1):
            sub = primes[i + 1] - primes[i]
            if sub < mini:
                mini = sub
                res = [primes[i], primes[i + 1]]  

        return res
