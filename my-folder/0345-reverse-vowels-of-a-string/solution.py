class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        # res = []
        # for char in s:
        #     if char in vowels:
        #         res.append(char)
        # print(res)
        # res.reverse()
        # print(res)
        # ans = []
        # i = 0
        # for char in s:
        #     if char in vowels:
        #         if i < len(res):
        #             ans.append(res[i])
        #             i += 1
        #         else:
        #             ans.append(char)
        #     else:
        #         ans.append(char)

        # ans = "".join(ans)
        # return ans
        i = 0
        j = len(s) - 1
        s_list = list(s)
        while i < j:
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
            elif s_list[i] not in vowels:
                i += 1
            elif s_list[j] not in vowels:
                j -= 1
            
        s = "".join(s_list)
        return s
