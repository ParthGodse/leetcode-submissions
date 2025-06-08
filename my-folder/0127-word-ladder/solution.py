class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        queue = deque()
        queue.append(beginWord)
        
        # Create a set to mark visited genes
        visited = set()
        visited.add(beginWord)

        count = 1
        
        # Perform BFS
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextword = word[:j] + c + word[j+1:]
                        if nextword in wordset and nextword not in visited:
                            visited.add(nextword)
                            queue.append(nextword)
            count += 1
        
        return 0
