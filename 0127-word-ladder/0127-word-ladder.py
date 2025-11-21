class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        
        if endWord not in words:
            return 0
        
        visit = set()
        count = 1
        q = deque([beginWord])
        visit.add(beginWord)
        # valid = 'abcdefghijklmnopqrstuvwxyz'
        n = len(beginWord)
        adj = defaultdict(list)
        for word in words:
            for j in range(n):
                new_word = word[:j] + '*' + word[j + 1:]
                adj[new_word].append(word) 

        while q:

            size = len(q)

            for i in range(size):
                word = q.popleft()

                if word == endWord:
                    return count

                for j in range(n):
                    new_word = word[:j] + '*' + word[j + 1:]
                    for new in adj[new_word]:
                        if new not in visit:
                            q.append(new)
                            visit.add(new)

            count += 1
        return 0