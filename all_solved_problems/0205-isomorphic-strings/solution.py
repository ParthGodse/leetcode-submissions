class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # return sorted(Counter(s).values()) == sorted(Counter(t).values())
        # ind1 = [0] * 200
        # ind2 = [0] * 200
        # n, m = len(s), len(t)
        # if n != m:
        #     return False

        # for i in range(n):
        #     if ind1[ord(s[i])] != ind2[ord(t[i])]:
        #         return False

        #     ind1[ord(s[i])] = i + 1
        #     ind2[ord(t[i])] = i + 1
        # return True
        ind1, ind2 = [], []
        for i in s:
            ind1.append(s.index(i))
        for j in t:
            ind2.append(t.index(j))
        if ind1 == ind2:
            return True
        return False
