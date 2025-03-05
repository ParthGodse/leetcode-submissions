class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1 + str2 != str2 + str1:
        #     return ""

        # gcd = math.gcd(len(str1), len(str2))

        # return str1[:gcd]
        if len(str1) > len(str2):
            str1 , str2 = str2, str1

        for i in range(len(str1), 0, -1):
            prefix = str1[:i]

            if str1 == prefix * (len(str1) // len(prefix)) and str2 ==prefix * (len(str2) // len(prefix)):
                return prefix

        return ""
