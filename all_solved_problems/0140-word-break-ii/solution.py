class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # words = set(wordDict)
        # res = {}

        # def dfs(start):
        #     if start in res:
        #         return res[start]

        #     if start == len(s):
        #         return [""]

        #     sentences = []
        #     for end in range(start + 1, len(s) + 1):
        #         word = s[start:end]
        #         if word in words:
        #             rest_sentences = dfs(end)
        #             for rest in rest_sentences:
        #                 sentence = word + (" " + rest if rest else "")
        #                 sentences.append(sentence)

        #     res[start] = sentences
        #     return sentences
        # return dfs(0)
        words = set(wordDict)
        res = {}

        def dfs(start):
            if start in res:
                return res[start]

            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words:
                    rest_sentences = dfs(end)
                    for rest in rest_sentences:
                        sentence = s[start:end] + (" " + rest if rest else "")
                        sentences.append(sentence)
            res[start] = sentences
            return sentences
        return dfs(0)
