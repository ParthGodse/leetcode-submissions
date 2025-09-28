class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # n = len(arr)
        # res = []
        # MOD = 1000000007
        # count = 0

        # for i in range(n):
        #     summ = 0
        #     for j in range(i, n):
        #         summ += sum(int(digit) for digit in str(arr[j])) 
        #         # summ %= MOD 
        #         if summ % 2 != 0:
        #             count += 1 

        # return count
        oddCount, prefixSum, mod = 0, 0, 10**9 + 7
        for a in arr:
            prefixSum += a
            oddCount += prefixSum % 2
        oddCount += (len(arr) - oddCount) * oddCount
        return oddCount % mod
