class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        n = len(s)

        res = []

        for start in range(word_len):  # offsets 0,1,...word_len-1
            left = start
            curr_count = Counter()
            matched = 0

            for right in range(start, n, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    curr_count[word] += 1
                    matched += 1

                    # shrink if more than needed
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        matched -= 1
                        left += word_len

                    # if all words matched
                    if matched == len(words):
                        res.append(left)
                else:
                    curr_count.clear()
                    matched = 0
                    left = right + word_len

        return res