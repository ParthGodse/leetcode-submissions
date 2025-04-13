class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(base, exp, mod):
            res = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % mod
                base = (base * base) % mod
                exp //= 2
            return res

        evens = (n + 1) // 2
        odds = n // 2

        return(power(5, evens, MOD) * power(4, odds, MOD)) % MOD
